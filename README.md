# 🔒 FastAPI 기반 실시간 라벨링 작업 접근 제어 시스템

> 여러 사용자가 동시에 라벨링 작업을 수행할 때, **프로젝트별 단일 사용자 접근**, **파일 단위 잠금/해제**, **실시간 메시지 브로드캐스트** 기능을 제공하는 FastAPI + WebSocket 기반 백엔드 시스템입니다.

---

## 📌 프로젝트 목적

라벨링 웹사이트에서 다음 요구사항을 만족하기 위해 제작된 실시간 접근 제어 시스템입니다:

- 프로젝트별 동일한 파일에 여러 사용자가 접근하지 못하도록 제어
- 사용자별 접근 중인 파일을 추적하고 상태 표시
- 실시간 메시지 전송 및 브로드캐스트 (접속/해제/메시지)
- FastAPI WebSocket 기반 구조

---

## 🗂️ 프로젝트 구조

│app <br>
├── main.py <br>
├── routers/ <br>
│   ├── file_lock.py <br>
│   └── websocket.py <br>
├── services/ <br>
│   ├── lock_service.py <br>
│   └── websocket_service.py <br>
└── utils/ <br>
    └── redis.py <br>
