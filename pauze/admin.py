from django.contrib import admin
from .models import PauzeContent

@admin.register(PauzeContent)
class PauzeContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'last_edited')