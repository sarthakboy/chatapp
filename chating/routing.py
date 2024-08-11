from django.urls import path , include
from chating.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("chat/" , ChatConsumer.as_asgi()) , 
] 
