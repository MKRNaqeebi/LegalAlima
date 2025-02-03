"""
This file contains the serializers for the models in the interface app.
"""
from rest_framework import serializers

from interface.models import Chat, TokenParams, Message, DeployToken

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """
    class Meta:
        """
        Meta class for the MessageSerializer
        """
        model = Message
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    """
    Serializer for the Chat model.
    """
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        """
        Meta class for the ChatSerializer
        """
        model = Chat
        fields = '__all__'

class TokenParamsSerializer(serializers.ModelSerializer):
    """
    Serializer for the TokenParams model.
    """
    class Meta:
        """
        Meta class for the TokenParamsSerializer
        """
        model = TokenParams
        fields = '__all__'


class DeployTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for the DeployToken model.
    """
    class Meta:
        """
        Meta class for the DeployTokenSerializer
        """
        model = DeployToken
        fields = '__all__'
