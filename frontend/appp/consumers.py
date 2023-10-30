from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
import asyncio
from time import sleep

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websockets are connect with client...',event)
        self.send({
            'type':'websocket.accept',
        })
    
    def websocket_receive(self,event):
        print('Websocket recieve cliend massage...',event)
        for i in range(1,6):
            self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            sleep(1)
            
    
    def websocket_disconnect(self,event):
        print('Websocket & cliend Disconnected...',event)
        raise StopConsumer
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('Websockets are connect with client...',event)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self,event):
        print('Websocket recieve cliend massage...',event)
        for i in range(1,6):
            await self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self,event):
        print('Websocket & cliend Disconnected...',event)
        raise StopConsumer
    