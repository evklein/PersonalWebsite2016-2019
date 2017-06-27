from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^Steganography', views.steganography, name='Steganography'),
    url(r'^Recording', views.recording, name='Recording')
]
