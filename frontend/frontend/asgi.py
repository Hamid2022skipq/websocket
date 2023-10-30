import os
from channels.routing import URLRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from appp.route import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frontend.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        websocket_urlpatterns
    )
})
