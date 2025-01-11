import os
from datetime import datetime
import pytz
from dotenv import load_dotenv
from notion_client import Client

class NotionLogger:
    def __init__(self):
        load_dotenv()
        self.notion = Client(auth=os.getenv("NOTION_API_KEY"))
        self.database_id = os.getenv("NOTION_DATABASE_ID")
        self.kst = pytz.timezone('Asia/Seoul')

    def log_error(self, error_data):
        """
        에러 로그를 Notion 데이터베이스에 기록
        
        error_data 형식:
        {
            "timestamp": "2025-01-08 04:41:34",  # 에러 발생 시간 (마이크로초 없는 형식도 지원)
            "command": "[2025-01-08 04:41:34.210597] 작업 test 시작 (PID: 8332)",  # 실행 명령어
            "error": "[2025-01-08 04:41:34.210718] 작업 test 에러 발생: Error: 강제로 발생된 에러입니다.",  # 에러 메시지
            "full_log": "전체 로그 내용"  # 전체 로그
        }
        """
        try:
            # 타임스탬프 형식 처리 (마이크로초가 있는 경우와 없는 경우 모두 지원)
            try:
                timestamp = datetime.strptime(error_data["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
            except ValueError:
                timestamp = datetime.strptime(error_data["timestamp"], "%Y-%m-%d %H:%M:%S")
            
            timestamp_kst = self.kst.localize(timestamp)
            
            # Notion 데이터베이스에 새 페이지 생성
            new_page = self.notion.pages.create(
                parent={"database_id": self.database_id},
                properties={
                    "Error": {
                        "title": [
                            {
                                "text": {
                                    "content": error_data["error"]
                                }
                            }
                        ]
                    },
                    "Timestamp": {
                        "date": {
                            "start": timestamp_kst.isoformat()
                        }
                    },
                    "Command": {
                        "rich_text": [
                            {
                                "text": {
                                    "content": error_data["command"]
                                }
                            }
                        ]
                    }
                },
                children=[
                    {
                        "object": "block",
                        "type": "heading_2",
                        "heading_2": {
                            "rich_text": [{"text": {"content": "Full Log"}}]
                        }
                    },
                    {
                        "object": "block",
                        "type": "code",
                        "code": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": error_data["full_log"]
                                    }
                                }
                            ],
                            "language": "plain text"
                        }
                    }
                ]
            )
            print(f"Error logged to Notion: {error_data['error']}")
        except Exception as e:
            print(f"Failed to log to Notion: {str(e)}")

if __name__ == "__main__":
    # Example usage
    logger = NotionLogger()
    error_data = {
        "timestamp": "2025-01-08 04:41:34",  # 마이크로초 없는 형식 테스트
        "command": "[2025-01-08 04:41:34.210597] 작업 test 시작 (PID: 8332)",
        "error": "[2025-01-08 04:41:34.210718] 작업 test 에러 발생: Error: 강제로 발생된 에러입니다.",
        "full_log": "전체 로그 내용"
    }
    logger.log_error(error_data)
