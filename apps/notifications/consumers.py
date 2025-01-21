from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Notification

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            f"user_{self.scope['user'].id}",
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f"user_{self.scope['user'].id}",
            self.channel_name
        )

    async def notify(self, event):
        await self.send_json({
            'type': 'notification',
            'message': event['message']
        }) 
from channels.db import database_sync_to_async
from .models import Notification

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            f"user_{self.scope['user'].id}",
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f"user_{self.scope['user'].id}",
            self.channel_name
        )

    async def notify(self, event):
        await self.send_json({
            'type': 'notification',
            'message': event['message']
        }) 