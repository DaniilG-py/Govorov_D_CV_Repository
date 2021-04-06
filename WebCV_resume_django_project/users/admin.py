from django.contrib import admin

from .models import CustomUser, UserMessage, AnonymousUser, AnonymousMessage


admin.site.register(CustomUser)
admin.site.register(UserMessage)
admin.site.register(AnonymousUser)
admin.site.register(AnonymousMessage)
