import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Mesa
from asgiref.sync import sync_to_async

class MesaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.loop_task = asyncio.create_task(self.send_mesas_data_continuously())

    async def disconnect(self, close_code):
        if hasattr(self, 'loop_task'):
            self.loop_task.cancel()

    async def send_mesas_data_continuously(self):
        while True:
            await asyncio.sleep(1)  # Atualize a cada segundo
            await self.send_mesas_data()

    async def send_mesas_data(self):
        mesas_data = await self.get_all_mesas_data()
        await self.send(text_data=json.dumps({
            'type': 'mesas_update',
            'mesas': mesas_data
        }))

    @sync_to_async
    def get_all_mesas_data(self):
        mesas = Mesa.objects.all().order_by('mesa')
        mesas_data = [{
            'mesa': mesa.mesa,
            'total_valor': str(mesa.total_valor),
            'valor_recebido': str(mesa.valor_recebido),
        } for mesa in mesas]
        return mesas_data