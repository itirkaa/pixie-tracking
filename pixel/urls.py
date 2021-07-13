from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('pixel.gif', views.pixel_view, name='image_load'),
]
