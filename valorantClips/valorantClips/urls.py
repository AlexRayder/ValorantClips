"""
URL configuration for valorantClips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_valorant import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'), # Ruta para la vista inicio
    path('personajes/', views.personajes, name='personajes'),
    path('subirVideo/', views.subir_video, name ='subirVideo'),
    path('mostrar_videos/', views.mostrar_videos, name='mostrar_videos'),
    path('video/list/', views.video_list, name='video_list'),
    path('video/<int:video_id>/delete/', views.delete_video, name='delete_video'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)