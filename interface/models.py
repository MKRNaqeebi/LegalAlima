"""
Models for the interface app
"""
from django.db import models
from django.contrib.auth import get_user_model


class Chat(models.Model):
    """
    Chat model
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"# {self.name}"


class TokenParams(models.Model):
    """
    TokenParams model
    """
    NETWORK_CHOICES = [
        ('binance', 'Binance Smart Chain'),
        ('ethereum', 'Ethereum'),
        ('solana', 'Solana')
    ]
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    total_supply = models.IntegerField(default=20000000)
    decimals = models.IntegerField(default=18)
    network = models.CharField(max_length=100, choices=NETWORK_CHOICES)
    contract_standard = models.CharField(max_length=100, default="ERC20")
    liquidity_allocation = models.IntegerField(default=100)
    staking_rewards = models.IntegerField(default=100)
    governance_mechanism = models.CharField(max_length=100, default="DAO")
    transaction_fees = models.IntegerField(default=100)
    burn_mechanism = models.CharField(max_length=100, default="Deflationary")
    deflationary_or_inflationary = models.CharField(max_length=100, default="Deflationary")
    team_marketing_allocation = models.IntegerField(default=100)
    vesting_schedules = models.CharField(max_length=100, default="Yes")
    utility_use_cases = models.CharField(max_length=100, default="Yes")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.symbol}"


class DeployToken(models.Model):
    """
    DeployToken model
    """
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    token_params = models.ForeignKey(TokenParams, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    transaction_hash = models.CharField(max_length=512, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.token_params.name}: {self.address}"


class Message(models.Model):
    """
    Message model
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant')
    ]
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='1')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.content}"
