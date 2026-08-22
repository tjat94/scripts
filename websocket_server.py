import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        print("received:", message)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8080):
        await asyncio.Future()

asyncio.run(main())