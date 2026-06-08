import json
from django.shortcuts import render
from django.utils.timezone import localtime
from .models import ShoutwallMessage

def format_time(dt):
    if not dt: return ""
    return localtime(dt).strftime("%H:%M on %d/%m/%Y")

def index(request):
    data = PauzeContent.get_singleton()
    return render(request, 'shoutwall.html', {
        "title": data.title,
        "subtitle": data.subtitle,
        "content": data.content,
        "time_formatted": format_time(data.last_edited)
    })