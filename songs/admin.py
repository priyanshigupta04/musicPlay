# filepath: /c:/here/Projects/music_player/songs/admin.py
from django.contrib import admin
from .models import Playlist, Song


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_songs')  # Use ID and song details to display playlists
    fields = ('songs',)

    def get_songs(self, obj):
        return ", ".join([song.title for song in obj.songs.all()])
    get_songs.short_description = 'Songs'

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')