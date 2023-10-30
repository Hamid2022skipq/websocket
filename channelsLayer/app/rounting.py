from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/sc/<str:groupName>/', MySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupName>/', MyAsyncConsumer.as_asgi())
]
