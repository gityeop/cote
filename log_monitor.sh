#!/bin/bash

# 스크립트 디렉토리 경로
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 로그 파일 경로 설정
log_file="$SCRIPT_DIR/output.log"
output_file="$SCRIPT_DIR/error_logs.json"
temp_file="/tmp/error_temp.json"

# Python 스크립트 경로
notion_logger="$SCRIPT_DIR/notion_logger.py"

# Notion에 로그 전송 함수
send_to_notion() {
    local timestamp="$1"
    local command="$2"
    local error_msg="$3"
    local full_log="$4"
    
    # JSON 문자열을 이스케이프
    command_escaped=$(echo "$command" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))')
    error_escaped=$(echo "$error_msg" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))')
    full_log_escaped=$(echo "$full_log" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))')
    
    # Python 스크립트 실행
    PYTHONPATH="$SCRIPT_DIR" python3 - << EOF
import sys
import os
import json
from datetime import datetime
sys.path.append("$SCRIPT_DIR")

from notion_logger import NotionLogger

try:
    error_data = {
        "timestamp": "$timestamp",
        "command": ${command_escaped},
        "error": ${error_escaped},
        "full_log": ${full_log_escaped}
    }
    logger = NotionLogger()
    logger.log_error(error_data)
    print("Successfully logged to Notion")
except Exception as e:
    print(f"Failed to log to Notion: {str(e)}")
EOF
}

# 로그 파일 디렉토리가 없으면 생성
mkdir -p "$(dirname "$log_file")"
touch "$log_file"

# 출력 파일 디렉토리 생성
mkdir -p "$(dirname "$output_file")"

echo "[$(date '+%Y-%m-%d %H:%M:%S.N')] 로그 모니터링 시작 (모니터링 범위: $SCRIPT_DIR)"

# 현재 세션의 로그를 저장할 임시 배열
declare -a current_session_log=()
current_command=""
error_detected=false
error_message=""
in_traceback=false

# 로그 파일 모니터링 및 에러 정보 추출 (새로운 라인만)
tail -n 0 -F "$log_file" | while IFS= read -r line; do
    # 현재 라인을 세션 로그에 추가
    current_session_log+=("$line")
    
    # Command 실행 감지
    if [[ "$line" =~ ^\[.*\]\ Command:\ .* ]]; then
        current_command="$line"
        current_session_log=("$line")
        error_detected=false
        error_message=""
        in_traceback=false
    fi
    
    # Traceback 시작 감지
    if [[ "$line" =~ ^Traceback.*last\):.* ]]; then
        in_traceback=true
        error_detected=true
        error_message="$line"
        continue
    fi
    
    # Traceback 내용 수집
    if [[ "$in_traceback" == true ]]; then
        if [[ "$line" =~ ^[A-Za-z]+Error:.* ]]; then
            error_message="$error_message\n$line"
            in_traceback=false
            
            # 타임스탬프 생성
            timestamp=$(date '+%Y-%m-%d %H:%M:%S')
            
            # 에러 정보 JSON 생성
            error_json=$(python3 -c "import json; print(json.dumps({'timestamp': '$timestamp', 'command': '$current_command', 'log': '${current_session_log[@]}', 'error': '$error_message'}))")
            
            # JSON 파일에 저장
            if [ ! -s "$output_file" ]; then
                echo "[$error_json]" > "$output_file"
            else
                jq --arg new "$error_json" '. + [$new | fromjson]' "$output_file" > "$temp_file" && mv "$temp_file" "$output_file"
            fi
            
            # Notion에 에러 로그 전송
            full_log=$(printf '%s\n' "${current_session_log[@]}")
            send_to_notion "$timestamp" "$current_command" "$error_message" "$full_log"
            
            echo "[$(date '+%Y-%m-%d %H:%M:%S.N')] 에러 감지됨: $error_message"
        else
            error_message="$error_message\n$line"
        fi
    fi
    
    # 일반 에러 메시지 감지
    if [[ "$line" =~ "에러 발생: Error:" ]]; then
        error_detected=true
        error_message="$line"
        
        # 타임스탬프 추출
        timestamp=$(echo "$line" | grep -o "\[[0-9\-]* [0-9:.]*\]" | tr -d '[]')
        
        # 에러 정보 JSON 생성
        error_json=$(python3 -c "import json; print(json.dumps({'timestamp': '$timestamp', 'command': '$current_command', 'log': '${current_session_log[@]}', 'error': '$error_message'}))")
        
        # JSON 파일에 저장
        if [ ! -s "$output_file" ]; then
            echo "[$error_json]" > "$output_file"
        else
            jq --arg new "$error_json" '. + [$new | fromjson]' "$output_file" > "$temp_file" && mv "$temp_file" "$output_file"
        fi
        
        # Notion에 에러 로그 전송
        full_log=$(printf '%s\n' "${current_session_log[@]}")
        send_to_notion "$timestamp" "$current_command" "$error_message" "$full_log"
        
        echo "[$(date '+%Y-%m-%d %H:%M:%S.N')] 에러 기록됨: $error_message"
    fi
done
