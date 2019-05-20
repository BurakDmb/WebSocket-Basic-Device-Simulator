import asyncio
import websockets

async def get_temp():
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        await websocket.send("house/sensor,get_temp")

        result = await websocket.recv()
        print("Result: ", result)

asyncio.get_event_loop().run_until_complete(get_temp())