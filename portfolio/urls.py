from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^dj-say', views.dj_say, name='dj-say'),
    url(r'^Kill-Switch/', views.kill_switch, name='Kill-Switch'),
    url(r'^Song-Friend/', views.song_friend, name='Song-Friend'),
    url(r'^Stegory/', views.stegory, name='Stegory'),
    url(r'^Hex-Helper/', views.hex_helper, name='Hex-Helper'),
    url(r'^aes0p/', views.aes0p, name='aes0p'),
    url(r'^Ghostly/', views.ghostly, name='ghostly'),
]
