from django.shortcuts import render,redirect
from signupforms.models import Registrations
from uploadsongs.models import SongUploads
# Create your views here.
def uploads_view(request):
    try:
        current_user = request.COOKIES['logedinuser']
    except:
        return redirect("/")

    if request.method == 'POST':
        songtitle = request.POST['songtitle']
        songalbum = request.POST['songalbum']
        songgenre = request.POST['songgonre']
        songfile = request.FILES['songfile']
        songlyrics = request.POST['lyrices']
        artists = Registrations.objects.get(username=current_user)
        new_song = SongUploads(artists=artists,songalbum = songalbum,songtitle=songtitle,songtype=songgenre,songfile = songfile,songlyrics=songlyrics)
        new_song.save()
        return redirect('/uploadsongs/')
    context = {
        'title':'music player | uploads'
    }
    return render(request, "uploads.html", context)