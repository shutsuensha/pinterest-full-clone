from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from .manager import manager
from typing import Optional



def register_websocket(app: FastAPI):
    @app.websocket("/ws/{chat_id}/{user_id}")
    async def chat_endpoint(websocket: WebSocket, chat_id: int, user_id: int, chat_connection: bool | None = None):
        await manager.connect(websocket, chat_id, user_id, chat_connection)
        try:
            while True:
                data = await websocket.receive_json()
                await manager.send_message(data, chat_id, user_id)
        except WebSocketDisconnect:
            manager.disconnect(chat_id, user_id, chat_connection)