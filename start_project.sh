#!/bin/bash

# 프로젝트 디렉토리로 이동
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$PROJECT_DIR"

# 가상환경 활성화
source venv/bin/activate

# 프로젝트별 zsh 설정 로드
if [ -f ".zshrc.local" ]; then
    # 새로운 zsh 세션 시작
    exec zsh -c "source .zshrc.local; zsh"
else
    echo "Error: .zshrc.local not found"
    exit 1
fi
