from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

from .views import *
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^userdetail/$', UserDetailView, name='userdetail' ),
    url(r'^logout/$', views.logout,{'next_page': '/'}),

]
