"""
This file contains the URL patterns for the interface app.
"""
from django.urls import path
from interface.views import MessageView, ChatView, index, DeployTokenView, TokenParamsView

urlpatterns = [
    path('api/messages/', MessageView.as_view(), name='message-list-create'),
    path('api/chats/', ChatView.as_view(), name='chat-list-create'),
    path('api/deploy-tokens/', DeployTokenView.as_view(), name='deploy-token-list-create'),
    path('api/token-params/', TokenParamsView.as_view(), name='token-params-list'),
    path('', index, name='index'),
]
