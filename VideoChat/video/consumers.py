from channels.generic.websocket import AsyncJsonWebsocketConsumer


class VideoChat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.connect()

    async def receive_json(self, content):
        if(content['command'] == 'join_room'):
            await self.channel_layer.group_add(content["room"] , self.channel_name)

        elif (content['command'] == 'join'):
            await self.channel_layer.group_send(content['room'],{
                'type':'join.message'
            })

        elif (content['command'] == 'offer'):
            await self.channel_layer.group_send(content['room'],{
                'type':'offer.message',
                'offer':content['offer']
            })

    async def join_message(self , event):
        await self.send_json({
            'command':'join'
        }) 


    async def offer_message(self , event):
        await self.send_json({
            'command':'offer',
            'offer':event['offer']
        })