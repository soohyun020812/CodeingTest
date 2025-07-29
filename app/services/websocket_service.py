from fastapi import WebSocket
from typing import Dict, List
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = defaultdict(list)

    async def connect(self, project_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[project_id].append(websocket)
        await self.broadcast(project_id, f"[{project_id}] 사용자 연결됨")

    async def disconnect(self, project_id: str, websocket: WebSocket):
        if websocket in self.active_connections[project_id]:
            self.active_connections[project_id].remove(websocket)
            await self.broadcast(project_id, f"[{project_id}] 사용자 연결 해제됨")

    async def broadcast(self, project_id: str, message: str):
        for connection in self.active_connections[project_id]:
            await connection.send_text(message)

manager = ConnectionManager()

