from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket connected...', event)
        self.send({
            'type': 'websocket.accept'
        })
        # print('channels Layer...', self.channel_layer)
        # print('channels name...', self.channel_name)
        # # converting from async to sync
        # async_to_sync(self.channel_layer.group_add)(
        #     'programmer', self.channel_name)

    def websocket_receive(self, event):
        print('Websocket received...', event)
        print('Type is : ', type(event['text']))
        print('Meesage is : ', json.loads(event['text'])['msg'])
        async_to_sync(self.channel_layer.group_send)('programmers', {
            'type': 'chat.message',
            'message': event['text'],
        })

        def chat_message(self, event):
            print('Event...', event)
            print('Actual Data', event('message'))
            print('Type of Actual Data', type(event('message')))

        self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        # print('channels Layer...', self.channel_layer)
        # print('channels name...', self.channel_name)
        # async_to_sync(self.channel_layer.group_discard)(
        #     'programmer', self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket connected...', event)
        self.GroupName = self.scope['url_route']['kwargs']['groupName']
        print('Group Name :', self.GroupName)

        # print('channels Layer...', self.channel_layer)
        # print('channels name...', self.channel_name)

        # await self.channel_layer.group_add)(
        #     'self.GroupName', self.channel_name)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('Websocket received...', event)
        print('Type is : ', type(event['text']))
        print('Meesage is : ', json.loads(event['text'])['msg'])
        # self.GroupName = self.scope['url_route']['kwargs']['groupName']

        # await self.channel_layer.group_send('self.GroupName', {
        #     'type': 'chat.message',
        #     'message': event['text'],
        # })

        # def chat_message(self, event):
        #     print('Event...', event)
        #     print('Actual Data',event('message'))
        #     print('Type of Actual Data',type(event('message')))

        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    async def websocket_disconnect(self, event):
        print('Websocket disconnected...', event)
        # self.GroupName = self.scope['url_route']['kwargs']['groupName']
        # print('channels Layer...', self.channel_layer)
        # print('channels name...', self.channel_name)
        # await self.channel_layer.group_discard(
        #     'self.GroupName', self.channel_name)

        raise StopConsumer()
