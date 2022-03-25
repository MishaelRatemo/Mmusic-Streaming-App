from django.shortcuts import render,redirect
from uploadsongs.models import SongUploads
from signupforms.models import Registrations
from homepage.models import Favourites
# Create your views here.
def home_view(request):
    try:
        current_user = request.COOKIES['logedinuser']
    except:
        return redirect("/")
    role = Registrations.objects.get(username=current_user)
    try:
        songs = SongUploads.objects.all().order_by('-id')
    except:
        songs = 'nosongs'
    context = {
        'title': 'music player',
        'songs':songs,
        'role':role
    }
    return render(request, "home.html", context)

def addfavs_view(request, id):
    current_user = request.COOKIES['logedinuser']
    if current_user:
        pass
    else:
        return redirect("/")
    username = current_user
    song = SongUploads.objects.get(id = id)
    getfavs = Favourites.objects.filter(username=username, songfileid=song)
    if getfavs.exists():
        pass
    else:
        newfaves = Favourites(username=username, songfileid = song)
        newfaves.save()
    return redirect('/home/')

def getsong_lyrics(request, id):
    lyrics = SongUploads.objects.get(id = id)
    context = {
        'title':'Song lyrics',
        'lyrics':lyrics
    }
    return render(request, "lyrics.html", context)


def logout_view(request):
        user = request.COOKIES['logedinuser']
        response = redirect("/")
        response.delete_cookie("logedinuser")
        return response