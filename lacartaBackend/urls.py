"""
URL configuration for lacartaBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from apps.usuarios.views import register_asequible,register_recomendado,register_premium

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register_asequible/', register_asequible, name='register_asequible'),
    path('register_recomendado/', register_recomendado, name='register_recomendado'),
    path('register_premium/', register_premium, name='register_premium'),
    path('locals/', include('apps.locales.api.routers')),
    path('promo/', include('apps.ofertas.api.routers')),
    path('booking/', include('apps.reservas.api.routers')),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) 

