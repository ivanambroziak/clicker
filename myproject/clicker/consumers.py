import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatMessage

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'clicker_chat'
        self.room_group_name = f'chat_{self.room_name}'

        try:
            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            logger.info(f"WebSocket connected: {self.channel_name}")
        except Exception as e:
            logger.error(f"Error connecting WebSocket: {e}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            # Leave room group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            logger.info(f"WebSocket disconnected: {self.channel_name}")
        except Exception as e:
            logger.error(f"Error disconnecting WebSocket: {e}")

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '').strip()
            username = text_data_json.get('username', '').strip()

            # Validate input
            if not message or not username:
                await self.send(text_data=json.dumps({
                    'error': 'Повідомлення та ім\'я не можуть бути порожніми'
                }))
                return

            # Limit message length
            if len(message) > 500:
                message = message[:500]
            if len(username) > 50:
                username = username[:50]

            # Save message to database
            await self.save_message(username, message)

            # Get timestamp
            timestamp = await self.get_timestamp()

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'timestamp': timestamp
                }
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'error': 'Неправильний формат даних'
            }))
        except Exception as e:
            logger.error(f"Error receiving message: {e}")
            await self.send(text_data=json.dumps({
                'error': 'Помилка обробки повідомлення'
            }))

    async def chat_message(self, event):
        try:
            message = event['message']
            username = event['username']
            timestamp = event['timestamp']

            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'username': username,
                'timestamp': timestamp
            }))
        except Exception as e:
            logger.error(f"Error sending chat message: {e}")

    @database_sync_to_async
    def save_message(self, username, message):
        try:
            ChatMessage.objects.create(username=username, message=message)
        except Exception as e:
            logger.error(f"Error saving message to database: {e}")

    @database_sync_to_async
    def get_timestamp(self):
        from django.utils import timezone
        return timezone.now().strftime('%H:%M')