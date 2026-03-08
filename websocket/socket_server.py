import asyncio
import websockets

async def handle(websocket):

    async for message in websocket:

        print("User:", message)

        response = "Your appointment has been processed."

        await websocket.send(response)


start_server = websockets.serve(handle, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
