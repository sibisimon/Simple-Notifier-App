from channels.generic.websocket import AsyncJsonWebsocketConsumer


class EchoUserAndCommet(AsyncJsonWebsocketConsumer):
    """
    Consumer for connecting, disconnecting and sending data with channel
    """

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("user", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("user", self.channel_name)

    async def user_echo(self, event):
        await self.send_json(event)

