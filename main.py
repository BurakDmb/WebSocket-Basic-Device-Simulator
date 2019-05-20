### A simple physical sensor device simulator with using WebSocket communication protocol.
import asyncio
import websockets
from random import randint

async def get_temp(websocket, path):
    receive = await websocket.recv()
    split = receive.split(",")
    if split[0] == "house/sensor" and split[1] == "get_temp":

        temp = randint(30,45)    
        await websocket.send("house/sensor_result,"+str(temp))
        print("received message=" + receive + ", topic=" + split[0] +". Sent temp="+str(temp))

start_server = websockets.serve(get_temp, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()