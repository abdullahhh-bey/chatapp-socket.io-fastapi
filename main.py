from fastapi import FastAPI
import socketio

#it is simply making a compatible websocket transport server
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

app = FastAPI()

#it is combining the fastapi & socket.io
app = socketio.ASGIApp(sio, other_asgi_app=app)


@sio.on("connect")
async def connect(id):
    print(f"User:{id} connected")
    await sio.emit("message" , f"User:{id} enters the chat")
    
    
@sio.on("disconnect")
async def disconnect(id):
    print(f"User:{id} disconnected")
    await sio.emit("message" , f"User:{id} left the chat",  skip_sid=id) #it means that everyone get the mesage of disconnection excepts the one who disconnect


@sio.on("message")
async def message(name, data):
    print(f"{id} messsaged")
    await sio.emit("message" , f"{name}\n{data}\n")
    
