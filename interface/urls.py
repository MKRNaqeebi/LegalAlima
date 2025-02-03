"""
This file contains the URL patterns for the interface app.
"""
from django.urls import path
from interface.views import MessageView, ChatView, index

urlpatterns = [
    path('api/messages/', MessageView.as_view(), name='message-list-create'),
    path('api/chats/', ChatView.as_view(), name='chat-list-create'),
    path('', index, name='index'),
]
