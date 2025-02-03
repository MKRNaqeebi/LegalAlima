"""
This file contains the views for the interface app.
"""
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from interface.models import Message, Chat, TokenParams, DeployToken
from interface.serializers import (
    MessageSerializer, ChatSerializer, DeployTokenSerializer, TokenParamsSerializer)
from interface.utils import messages_to_gpt_format
from interface.chain_deploy import deploy_contract


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
        content = request.data.get('content')
        response = messages_to_gpt_format(content)
        chat_id = request.data.get('chat')
        chat = Chat.objects.get(id=chat_id)
        TokenParams.objects.create(
            name=response.get('name'),
            symbol=response.get('symbol'),
            total_supply=response.get('total_supply'),
            decimals=response.get('decimals'),
            network=response.get('network'),
            contract_standard=response.get('contract_standard'),
            liquidity_allocation=response.get('liquidity_allocation'),
            staking_rewards=response.get('staking_rewards'),
            governance_mechanism=response.get('governance_mechanism'),
            transaction_fees=response.get('transaction_fees'),
            burn_mechanism=response.get('burn_mechanism'),
            deflationary_or_inflationary=response.get('deflationary_or_inflationary'),
            team_marketing_allocation=response.get('team_marketing_allocation'),
            vesting_schedules=response.get('vesting_schedules'),
            utility_use_cases=response.get('utility_use_cases'),
            chat=chat
        )
        return super().create(request, *args, **kwargs)


class ChatView(ListCreateAPIView):
    """
    Chat view
    """
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
    permission_classes = [AllowAny]


class TokenParamsView(ListAPIView):
    """
    TokenParams view
    """
    serializer_class = TokenParamsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return TokenParams.objects.order_by('-id')[:5]


class DeployTokenView(ListCreateAPIView):
    """
    DeployToken view
    """
    serializer_class = DeployTokenSerializer
    queryset = DeployToken.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Override the create method to add the chat id
        """
        token_params = TokenParams.objects.get(id=request.data.get('token_params'))
        try:
            request.data['transaction_hash'] = str(deploy_contract(token_params))
        except Exception as error:
            request.data['transaction_hash'] = str(error)
        return super().create(request, *args, **kwargs)
