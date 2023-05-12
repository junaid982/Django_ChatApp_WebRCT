from channels.generic.websocket import AsyncJsonWebsocketConsumer


class VideoChat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.connect()

    async def receive_json(self, content):
        pass