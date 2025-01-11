# 로깅 시스템 설정 튜토리얼

이 튜토리얼은 새로운 프로젝트에서 자동 로깅 시스템을 설정하는 방법을 설명합니다.

## 1. 새 디렉토리 생성 및 파일 복사

먼저 새로운 디렉토리를 만들고 필요한 파일들을 복사합니다:

```bash
# 1. 새 디렉토리 생성
mkdir my_project
cd my_project

# 2. 필요한 파일들 복사
cp /Users/imsang-yeob/BOJ/.zshrc.local .
cp /Users/imsang-yeob/BOJ/log_monitor.sh .
cp /Users/imsang-yeob/BOJ/notion_logger.py .
```

## 2. Python 가상환경 설정

Notion 로깅을 위한 파이썬 패키지들을 설치합니다:

```bash
# 1. 가상환경 생성
python -m venv venv

# 2. 가상환경 활성화
source venv/bin/activate

# 3. 필요한 패키지 설치
pip install python-dotenv notion-client pytz
```

## 3. Notion API 설정

`.env` 파일을 생성하고 Notion API 키와 데이터베이스 ID를 설정합니다:

```bash
# .env 파일 생성
cat > .env << EOL
NOTION_API_KEY=your_notion_api_key_here
NOTION_DATABASE_ID=your_notion_database_id_here
EOL
```

## 4. 실행 권한 설정

스크립트 파일에 실행 권한을 부여합니다:

```bash
chmod +x log_monitor.sh
```

## 5. 로그 모니터링 시작

두 가지 방법으로 로그 모니터링을 시작할 수 있습니다:

### 방법 1: 셸 세션에 직접 적용
```bash
source .zshrc.local
```

### 방법 2: 백그라운드에서 로그 모니터 실행
```bash
./log_monitor.sh &
```

## 6. 사용 방법

이제 다음과 같이 작동합니다:

1. 모든 명령어 실행이 자동으로 기록됩니다:
```bash
python my_script.py  # 실행 결과와 에러가 output.log에 기록됨
```

2. 에러가 발생하면 자동으로 Notion에도 기록됩니다.

## 주의사항

1. `.env` 파일의 보안:
   - `.env` 파일에는 민감한 정보가 포함되므로 `.gitignore`에 추가하세요
   - Notion API 키를 안전하게 보관하세요

2. 로그 파일 관리:
   - `output.log` 파일이 너무 커지지 않도록 주기적으로 관리하세요

3. 가상환경:
   - 항상 가상환경이 활성화된 상태에서 작업하세요
   - `deactivate` 명령어로 가상환경을 비활성화할 수 있습니다

## 문제 해결

1. 로그가 기록되지 않는 경우:
   - `output.log` 파일의 권한을 확인하세요
   - `.zshrc.local`이 제대로 source 되었는지 확인하세요

2. Notion 로깅이 작동하지 않는 경우:
   - `.env` 파일의 설정을 확인하세요
   - 가상환경이 활성화되어 있는지 확인하세요
   - 필요한 패키지들이 설치되어 있는지 확인하세요

## 파일 설명

1. `.zshrc.local`: 
   - 셸 설정 파일
   - 모든 명령어와 그 결과를 자동으로 로깅

2. `log_monitor.sh`:
   - 로그 모니터링 스크립트
   - 에러를 감지하고 Notion에 기록

3. `notion_logger.py`:
   - Notion API를 사용하여 에러를 Notion 데이터베이스에 기록
   - 에러 발생 시간, 명령어, 에러 메시지 등을 저장

## 작동 방식

1. 명령어 실행 시:
   - 명령어가 `output.log`에 기록됨
   - 실행 결과가 터미널과 로그 파일에 동시에 출력됨

2. 에러 발생 시:
   - 에러가 `output.log`에 기록됨
   - `log_monitor.sh`가 에러를 감지
   - `notion_logger.py`가 에러를 Notion에 기록

이 설정을 완료하면 모든 명령어 실행과 에러가 자동으로 기록되며, 중요한 에러는 Notion 데이터베이스에도 기록됩니다.
