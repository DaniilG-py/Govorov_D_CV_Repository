from django.contrib import admin

from .models import (
                WorkingExperience,
                EducationExperience,
                CustomUser,
                AnonymousUser,
                AnonymousMessage,
            )


admin.site.register(WorkingExperience)
admin.site.register(EducationExperience)
admin.site.register(CustomUser)
admin.site.register(AnonymousUser)
admin.site.register(AnonymousMessage)
