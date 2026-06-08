# project/urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path("", include("shoutwall.urls")),
]

if DEBUG:
    urlpatterns.insert(0, path("__reload__/", include("django_browser_reload.urls")))