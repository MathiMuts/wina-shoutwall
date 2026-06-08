import json
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import localtime
from .models import PauzeContent

def format_time(dt):
    if not dt: return ""
    return localtime(dt).strftime("%H:%M on %d/%m/%Y")

def index(request):
    data = PauzeContent.get_singleton()
    return render(request, 'pauze.html', {
        "title": data.title,
        "subtitle": data.subtitle,
        "content": data.content,
        "time_formatted": format_time(data.last_edited)
    })

def pauze_api(request):
    data = PauzeContent.get_singleton()

    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            if 'subtitle' in payload:
                data.subtitle = payload['subtitle']
            if 'content' in payload:
                data.content = payload['content']
            data.save()
        except json.JSONDecodeError:
            pass 

    return JsonResponse({
        "subtitle": data.subtitle,
        "content": data.content,
        "time_formatted": format_time(data.last_edited)
    })