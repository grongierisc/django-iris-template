"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_config.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from main.views import CommunityCommentViewSet, CommunityPostViewSet, CommunityTagViewSet, IrisDemoViewSet
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'CommunityComment', CommunityCommentViewSet)
router.register(r'CommunityPost', CommunityPostViewSet)
router.register(r'CommunityTag', CommunityTagViewSet)
router.register(r'IrisDemo', IrisDemoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('openapi/', get_schema_view(
        title="Post and Comment API",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),

]
