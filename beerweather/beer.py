import asyncio
import websockets

async def hello():
        async with websockets.connect('ws://159.69.212.240:60805/') as websocket:
                while(1):
                        name = input("INPUT: ")
                        await websocket.send(name)
                        print("> {}".format(name))
                        greeting = await websocket.recv()
                        print("< {}".format(greeting))
asyncio.get_event_loop().run_until_complete(hello())
