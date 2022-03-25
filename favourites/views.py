from django.shortcuts import render
from homepage.models import Favourites
from signupforms.models import Registrations

# Create your views here.
def favourite_view(request):
    try:
        current_user = request.COOKIES['logedinuser']
    except:
        return redirect("/")
    try:
        songs = Favourites.objects.filter(username=current_user)
    except:
        songs = 'nosongs'
    role = Registrations.objects.get(username=current_user)
    context = {
        'title':'music player | favouirites',
        'songs':songs,
        'role':role
    }
    return render(request, "favourites.html", context)