# Topic - Consumer

from channels.consumer import AsyncConsumer,SyncConsumer


class MyAsyncConsumer(AsyncConsumer):
# class MySyncConsumer(SyncConsumer):
    async def websocket_connect(self, event):
    # def websocket_connect(self, event):
        print('Websocket connected...')

    async def websocket_receive(self, event):
    # def websocket_receive(self, event):
        print('Message Received... ')

    async def websocket_disconnect(self, event):
    # def websocket_disconnect(self, event):
        print('WebSocket Disconnected... ')
