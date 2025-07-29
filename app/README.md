# 🔒 FastAPI 기반 실시간 라벨링 작업 접근 제어 시스템

> 여러 사용자가 동시에 라벨링 작업을 수행할 때 **프로젝트별 단일 사용자 접근**, **파일 단위 잠금/해제**, **실시간 메시지 브로드캐스트** 기능을 제공하는 FastAPI + WebSocket 기반 백엔드 시스템입니다.

---

### 📌 프로젝트 목적

라벨링 웹사이트에서 다음 요구사항을 만족하기 위해 제작된 실시간 접근 제어 시스템입니다.

- 프로젝트별 동일한 파일에 여러 사용자가 접근하지 못하도록 제어
- 사용자별 접근 중인 파일을 추적하고 상태 표시
- 실시간 메시지 전송 및 브로드캐스트 (접속/해제/메시지)
- FastAPI WebSocket 기반 구조

---

### 🗂️ 프로젝트 구조

```
app/
├── main.py
├── routers/
│   ├── file_lock.py
│   └── websocket.py
├── services/
│   ├── lock_service.py
│   └── websocket_service.py
└── utils/
    └── redis.py
```

---

### 🚀 실행 방법** (bash)

1. 가상 환경 설정 및 의존성 설치
- python -m venv venv
- source venv/bin/activate  # Windows: venv\Scripts\activate
- pip install fastapi uvicorn
2. 서버 실행
- uvicorn main:app --reload
3. 클라이언트 테스트
- 브라우저에서 http://localhost:8000/static/index.html 접속 후 WebSocket 테스트 가능

---

### 🔧 트러블슈팅

**문제 1** : ```uvicorn``` 명령어가 실행되지 않음 
uvicorn : 'uvicorn' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 
**원인** : ```uvicorn```이 설치되지 않았거나, 가상환경이 활성화되지 않은 상태에서 실행 
**해결 방법** : 1. 가상환경 활성화 후 pip install uvicorn으로 설치 
                2. 또는 전역 설치 : (bash) ```pip install "uvicorn[standard]"``` 

**문제 2** : 클라이언트에서 메시지는 보냈는데 서버 메시지가 안 뜸 
**원인** : WebSocket URL 형식이 잘못되었거나, 서버-클라이언트가 같은 ```project_id```를 기준으로 브로드캐스트하지 않음 
**해결 방법** : 1. WebSocket 연결 경로를 ```/ws/{project_id}``` 형식으로 맞추고, 클라이언트에서 일관되게 동일한 ```project_id``` 사용 (예: ```project123```) 

**문제 3** : WebSocket 메시지가 수신되지 않음  
**원인** : 클라이언트에서 메시지는 전송하지만, ```onmessage``` 이벤트 핸들러가 정의되어 있지 않아 서버 응답이 화면에 표시되지 않음  
**해결 방법** : JavaScript에서 WebSocket의 ```onmessage``` 이벤트 리스너를 등록하여, 서버로부터 수신한 메시지를 DOM에 출력하도록 수정  
```javascript
socket.onmessage = function (event) {
    const msg = document.createElement("div");
    msg.textContent = event.data;
    messagesDiv.appendChild(msg);
};
