from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import file_lock, websocket

access_control = FastAPI()

# 라우터 등록
access_control.include_router(file_lock.router, prefix="/file")
access_control.include_router(websocket.router, prefix="/ws")

# 웹소켓 테스트용 HTML 페이지
@access_control.get("/")
async def get():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>WebSocket Test</title>
        </head>
        <body>
            <h1>WebSocket Echo Test</h1>
            <input id="messageInput" type="text" placeholder="메시지를 입력하세요"/>
            <button onclick="sendMessage()">보내기</button>
            <ul id="messages"></ul>
            <script>
                const projectId = "project123";  // 예시 project_id
                const ws = new WebSocket(`ws://localhost:8000/ws/connect/${projectId}`);
                ws.onmessage = (event) => {
                    const messages = document.getElementById("messages");
                    const message = document.createElement("li");
                    message.textContent = event.data;
                    messages.appendChild(message);
                };
                function sendMessage() {
                    const input = document.getElementById("messageInput");
                    ws.send(input.value);
                    input.value = "";
                }
            </script>
        </body>
    </html>
    """)
