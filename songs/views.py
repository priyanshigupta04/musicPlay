from django.shortcuts import render, redirect, get_object_or_404
from .models import Playlist, Song
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import default_storage




@csrf_protect
def create_playlist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            new_playlist = Playlist.objects.create(name=name)
            return redirect('playlist_detail', playlist_id=new_playlist.id)
    return redirect('playlist_list')

# View to show songs in a specific playlist (audio and artist name only)
def playlist_view(request):
    playlists = Playlist.objects.all()
    songs = Song.objects.all()
    return render(request, 'songs/playlist.html', {'playlists': playlists, 'songs': songs})

# View to show songs in a specific playlist
def playlist_detail_view(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    return render(request, 'songs/playlist_detail.html', {'playlist': playlist})

@csrf_protect
def add_to_playlist(request):
    if request.method == "POST":
        playlist_id = request.POST.get("playlist_id")
        song_id = request.POST.get("song_id")
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.add(song)  # Assuming a Many-to-Many relationship
        return redirect('playlist_list')  # Redirect after adding
    
def remove_song_from_playlist(request, playlist_id, song_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    song = get_object_or_404(Song, id=song_id)
    
    # Remove the song from the playlist
    playlist.songs.remove(song)

    # Redirect back to the playlist details page
    return redirect('playlist_detail', playlist_id=playlist.id)
@csrf_protect
def upload_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        audio_file = request.FILES.get('audio_file')
        
        if title and artist and audio_file:
            # Save the audio file
            file_name = default_storage.save(f'songs/{audio_file.name}', audio_file)
            
            # Create a new Song object
            new_song = Song.objects.create(
                title=title,
                artist=artist,
                audio_file=file_name
            )
            
            return redirect('playlist_list')
    
    return redirect('playlist_list')



