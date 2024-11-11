import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SessionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_code = self.scope['url_route']['kwargs']['session_code']
        self.group_name = f'session_{self.session_code}'

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')
        payload = data.get('payload')

        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'session_action',
                'action': action,
                'payload': payload
            }
        )

    # Receive message from group
    async def session_action(self, event):
        action = event['action']
        payload = event['payload']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'action': action,
            'payload': payload
        }))
