from django.conf.urls import include, url
from django.contrib import admin
from blogs import views


urlpatterns = [
    # Examples:
    url(r'^index/',views.index),
]
