"""opr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from api import views as api_views

urlpatterns = [
    url(r'^user/create/$', api_views.create_user, name='create-user'),
    url(r'^user/(?P<user_id>[0-9]+)/$', api_views.user, name='user'),
    url(r'^user/login/$)', api_views.login, name='login'),
    url(r'^user/auth/$)', api_views.auth_view, name='auth_view'),
    url(r'^user/logout/$)', api_views.logout, name='logout'),
    url(r'^user/loggedin/$)', api_views.loggedin, name='loggedin'),
    url(r'^user/invalid/$)', api_views.invalid_login, name='invalid_login'),
]
