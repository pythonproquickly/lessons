import asyncio
import websockets


async def chat(websocket, path):
    while True:
        msg = await websocket.recv()
        print(f"Received from Client: {msg}")

        msg = input("Send message to client(type 'q' to exit): ")
        if msg == "q":
            break
        await websocket.send(msg)


start_server = websockets.serve(chat, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
