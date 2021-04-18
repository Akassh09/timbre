from django.shortcuts import render, redirect
from .models import Song, Liked
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    song = Song.objects.all()
    return render(request,'index.html',{'songs':song})

@login_required(login_url='login')
def songs(request):
    song = Song.objects.all()
    return render(request,'songs.html',{'songs':song})

@login_required(login_url='login')
def listen_song(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'listen_song.html',{'songs':song})

@login_required(login_url='login')
def playlist(request):
    if request.method == 'POST':
        user = request.user
        video_id = request.POST['video_id']

        like = Liked(user=user, video_id=video_id)
        like.save()
        return redirect('/songs/{video_id}')

    return render(request,'playlist.html',{'like':like})

