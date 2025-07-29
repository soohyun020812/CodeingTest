from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.websocket_service import manager

router = APIRouter()

@router.websocket("/connect/{project_id}")
async def websocket_endpoint(websocket: WebSocket, project_id: str):
    await manager.connect(project_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # 클라이언트가 보낸 메시지를 프로젝트 내 모든 연결에 브로드캐스트
            await manager.broadcast(project_id, f"[{project_id}] 메시지: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(project_id, websocket)
        await manager.broadcast(project_id, f"[{project_id}] 사용자 연결 해제됨")

