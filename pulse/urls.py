"""
URL configuration for pulse project.

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
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from appointment.views import AppointmentViewSet
from professional.views import ProfessionalViewset

SchemaView = get_schema_view(
    openapi.Info(
        title="Pulse API",
        default_version='v1',
        description="A API for managing health professionals and appointments",
    ),
    public=True
)

urlpatterns = [
    path('professionals', ProfessionalViewset.as_view({
        'get': 'list',
        'post': 'create',
    }), name='professionals'),
    path('professionals/<str:pk>', ProfessionalViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='professional'),
    path('appointments', AppointmentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='appointments'),
    path('appointments/<str:pk>', AppointmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='appointment'),
    path('swagger/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
