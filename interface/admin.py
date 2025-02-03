"""
This file is used to register the models in the admin panel.
"""
from django.contrib import admin
from interface.models import Chat, TokenParams, Message
# Register your models here.

admin.site.register(Chat)
admin.site.register(TokenParams)
admin.site.register(Message)
