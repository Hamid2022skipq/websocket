from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Client Connected...', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('Client Message Received...', event['text'])
        for i in range(1,51):
            self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print('Connection losed :(')
        raise StopConsumer


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Client Connected...', event)
        await self.send({
            'type': 'websocket.accept'
        })
        

    async def websocket_receive(self, event):
        print('Client Message Received...', event['text'])
        for i in range(1,51):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print('Connection losed :(')
        raise StopConsumer
