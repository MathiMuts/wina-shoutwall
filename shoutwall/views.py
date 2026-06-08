from django.shortcuts import render, redirect
from .models import ShoutwallMessage

def index(request):
    if request.method == "POST":
        poster = request.POST.get("poster", "").strip()
        content = request.POST.get("content", "").strip()
        
        if poster and content:
            ShoutwallMessage.objects.create(
                poster=poster[:100], 
                content=content[:1000]
            )
            return redirect('shoutwall:index')

    messages = ShoutwallMessage.objects.all()

    return render(request, 'shoutwall.html', {
        "title": "Shoutwall",
        "messages": messages,
    })