import os
from channels.routing import URLRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from app.rounting import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelsLayer.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
    websocket_urlpatterns
    )
})
