from django.contrib import admin
from .models import UserRequest


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')


admin.site.register(UserRequest, UserRequestAdmin)
