from django.urls import path
from .consumers import MesaConsumer

websocket_urlpatterns = [
    path('ws/mesa_atualizacao/', MesaConsumer.as_asgi()),
]