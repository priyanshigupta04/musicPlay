# filepath: /c:/here/Projects/music_player/songs/models.py
from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    songs = models.ManyToManyField(Song, related_name='playlists')

    def __str__(self):
        return f"Playlist with {self.songs.count()} song(s)"
    



