from django.contrib import admin
from .models import ShoutwallMessage

@admin.register(ShoutwallMessage)
class ShoutwallMessageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'poster', 'content')