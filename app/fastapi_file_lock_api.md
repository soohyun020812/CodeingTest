> 이 문서는 ChatGPT를 통해 정리되었습니다.
# FastAPI 기반 파일 잠금 API

## 📁 프로젝트 개요

여러 사용자가 동시에 이미지 라벨링 작업을 수행하는 웹 서비스에서, 다음과 같은 문제를 해결하기 위한 FastAPI 기반 백엔드 API입니다.

- 프로젝트 내 동일 파일에 대해 여러 사용자가 동시에 작업하는 충돌 방지
- 사용자당 한 개의 파일만 동시에 작업하도록 제한
- 실시간 파일 잠금 상태 관리
- 일정 시간동안 작업 없을 시 자동 잠금 해제 처리

---

## 🔧 주요 기술 스택

- **Python 3.11**
- **FastAPI**: 비동기 API 서버 구현
- **Uvicorn**: ASGI 서버
- **Redis**: 파일 잠금 상태 관리 및 TTL 설정
- **Socket.IO (via `python-socketio`, `socket.io-client`)**: 실시간 통신
- **aiofiles**: 비동기 파일 처리

---

## ⚙️ 기능 설명

### 1. 파일 잠금 (Lock)
- 한 사용자가 특정 프로젝트의 파일을 선택하면 해당 파일에 대한 잠금 요청 전송
- Redis에 `"lock:{project_id}:{file_name}"` 키로 잠금 정보 저장
- 이미 잠금 상태일 경우, 잠금 사용자 정보 반환

### 2. 파일 잠금 해제 (Unlock)
- 사용자가 파일 작업을 종료하거나 일정 시간 이상 작업이 없을 경우 자동 해제
- `unlock_file` API 또는 TTL(Time-To-Live) 기반 자동 해제

### 3. 잠금 상태 조회
- 클라이언트가 특정 프로젝트의 모든 파일 잠금 상태 조회 가능
- 프론트엔드에서 실시간 표시 가능

### 4. 실시간 잠금/해제 알림
- 클라이언트가 WebSocket으로 서버와 연결
- 잠금/해제 시 관련 이벤트를 해당 방(room)의 클라이언트들에게 브로드캐스팅

---

## 🔌 API 명세

| Method | Endpoint                    | 설명                          |
|--------|-----------------------------|-------------------------------|
| POST   | `/lock`                     | 파일 잠금 요청                |
| POST   | `/unlock`                   | 파일 잠금 해제                |
| GET    | `/status/{project_id}`      | 프로젝트 내 파일 잠금 상태 조회 |

---

## 🔄 WebSocket 이벤트 명세

### ✅ 클라이언트 → 서버
- `join_project`: 프로젝트 방 입장
```json
{ "project_id": "1234", "user_id": "user1" }
```

- `leave_project`: 방 퇴장
- `heartbeat`: 주기적 신호로 TTL 연장 (예: 30초마다)

---

### 📢 서버 → 클라이언트
- `lock_acquired`
```json
{ "file": "image1.jpg", "user": "user1" }
```

- `lock_released`
```json
{ "file": "image1.jpg" }
```

---

## 🧪 테스트 및 사용법

### 1. 서버 실행

```bash
uvicorn main:app --reload
```

### 2. Swagger 문서
http://127.0.0.1:8000/docs

---

## ⚠️ 자주 겪는 문제 및 해결

### 문제 1: 잠금 상태 TTL이 초기화되지 않음
- 원인: 클라이언트가 heartbeat를 주기적으로 보내지 않음
- 해결: WebSocket 연결 후 일정 주기로 `heartbeat` 이벤트 전송

### 문제 2: 실시간 잠금 해제 이벤트 누락
- 원인: 사용자가 소켓 연결 종료 없이 브라우저 종료
- 해결: WebSocket 연결 끊김 감지 후 서버 측에서 자동 해제 처리

### 문제 3: WebSocket 메시지가 수신되지 않음
- 원인: 클라이언트에서 `onmessage` 핸들러 미설정
- 해결: 다음과 같이 등록

```javascript
ws.onmessage = (event) => {
    const messages = document.getElementById("messages");
    const message = document.createElement("li");
    message.textContent = event.data;
    messages.appendChild(message);
};
```

---

## 📂 프로젝트 구조 예시

```
.
├── main.py              # FastAPI 서버 실행
├── redis_manager.py     # Redis를 이용한 잠금 관리
├── websocket.py         # 실시간 소켓 이벤트 처리
├── schemas.py           # Pydantic 모델 정의
└── requirements.txt     # 의존성 패키지 목록
```

---

## 📌 기타 참고 사항

- `.md` 파일은 GitHub, GitLab, Notion 등에서 가독성이 좋고, 협업에 적합합니다.
- FastAPI는 Swagger 문서를 자동 생성하여 API 테스트를 쉽게 해줍니다.
- Redis의 TTL 기능을 활용하여 자동 잠금 해제 처리를 구현하였습니다.
