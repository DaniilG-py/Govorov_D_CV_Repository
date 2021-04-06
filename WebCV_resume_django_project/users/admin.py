from django.contrib import admin

from .models import CustomUser, UserMessage


admin.site.register(CustomUser)
admin.site.register(UserMessage)
