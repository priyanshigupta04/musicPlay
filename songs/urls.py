from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_view, name='playlist_list'),
    path('playlists/<int:playlist_id>/', views.playlist_detail_view, name='playlist_detail'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('add_to_playlist/', views.add_to_playlist, name='add_to_playlist'),
    path('playlist/<int:playlist_id>/remove_song/<int:song_id>/', views.remove_song_from_playlist, name='remove_song_from_playlist'),
    path('upload_song/', views.upload_song, name='upload_song'),


]