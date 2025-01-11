# Log Error Monitor

터미널 명령어 실행 시 발생하는 에러를 모니터링하고 Notion에 자동으로 기록하는 시스템입니다.

## 기능
- 실시간 터미널 명령어 로깅
- 에러 발생 시 자동 감지
- Notion 데이터베이스에 에러 로그 기록
- 타임스탬프 KST 기준 변환

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/gityeop/log_error.git
cd log_error
```

2. 패키지 설치
```bash
pip install -r requirements.txt
```

3. 환경변수 설정
`.env` 파일을 생성하고 다음 내용을 추가:
```
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id
```

## 사용 방법

1. 프로젝트 시작
```bash
./start_project.sh
```

2. 종료
터미널에서 `exit` 또는 `Ctrl+D`를 입력하면 로깅이 종료됩니다.

## 요구사항
- Python 3.9+
- Notion API 키
- Notion 데이터베이스
