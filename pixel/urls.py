from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pixel/$', views.pixel_view, name='image_load'),
]
