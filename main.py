from fastapi import FastAPI
import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

fastapi_app = FastAPI()
app = socketio.ASGIApp(sio, other_asgi_app=fastapi_app)



@sio.event
async def connect(sid, environ):
    print(f"User connected: {sid}")
    await sio.emit("message",{"user": "Server", "text": f"{sid[:4]} joined the chat"})


@sio.event
async def disconnect(sid):
    print(f"User disconnected: {sid}")
    await sio.emit("message", {"user": "Server", "text": f"{sid[:4]} left the chat"})


@sio.on("message")
async def message(sid, data):
    print(f"{data['user']}: {data['text']}")
    await sio.emit("message", data)  
