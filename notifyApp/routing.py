from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumer import EchoUserAndCommet

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("user-notifications/", EchoUserAndCommet),
    ])
})