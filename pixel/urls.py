from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('<str:pixel_id>', views.pixel_view, name='image_load'),
]
