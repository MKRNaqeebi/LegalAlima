"""
This file contains the views for the interface app.
"""
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from interface.models import Message, Chat
from interface.serializers import (MessageSerializer, ChatSerializer)
# from interface.utils import messages_to_gpt_format


def index(request):
    """
    Serve the index.html file
    """
    return render(request, 'index.html')


class MessageView(ListCreateAPIView):
    """
    Message view
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Override the create method to add the chat id
        """
        # content = request.data.get('content')
        # response = messages_to_gpt_format(content)
        # chat_id = request.data.get('chat')
        # chat = Chat.objects.get(id=chat_id)
        return super().create(request, *args, **kwargs)


class ChatView(ListCreateAPIView):
    """
    Chat view
    """
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    permission_classes = [AllowAny]
