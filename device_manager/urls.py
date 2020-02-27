"""device_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='User API')

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    # provide the most basic login/logout functionality
    url(r'^login/$', auth_views.LoginView.as_view(template_name='core/login.html'),
        name='core_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='core_logout'),
    path('', RedirectView.as_view(url='login/')),

    url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
    url(r'^api-docs/$', schema_view)
]
