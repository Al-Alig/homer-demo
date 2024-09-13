"""
This file is used to define the URL patterns for the project.
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from homer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('user.urls')),
    path('', include('entity.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
