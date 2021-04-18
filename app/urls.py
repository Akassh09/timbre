from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('songs/',views.songs,name='songs'),
    path('songs/<int:id>/',views.listen_song,name='listen_song'),
    path('playlist/',views.playlist,name='playlist'), 
    
]