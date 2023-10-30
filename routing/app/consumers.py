from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket connected...', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('Websocket received...', event)
        print('Meesage is : ',event['text'])
        self.send({
            'type':'websocket.send',
            'text':'Thank You Sir :)'
        })


    def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket connected...', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('Websocket received...', event)
        print('Meesage is 2 : ',event['text'])
        self.send({
            'type':'websocket.send',
            'text':'Thank You Sir :)'
        })

    async def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        raise StopConsumer()
