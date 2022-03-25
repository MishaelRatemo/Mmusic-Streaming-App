from django.shortcuts import render,redirect
from signupforms.models import Registrations

# Create your views here.
def profiles_view(request):
    try:
        current_user = request.COOKIES['logedinuser']
    except:
        return redirect("/")
    profiles = Registrations.objects.get(username=current_user)
    role = Registrations.objects.get(username=current_user)
    context = {
        'title':'music player | profile',
        'profiles':profiles,
        'role':role
    }
    return render(request, "profiles.html", context)

def update_view(request):
    current_user = request.COOKIES['logedinuser']
    if current_user:
        pass
    else:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['usernames']
        userimage = request.FILES['userimage']
        passwords = request.POST['password']
        # getuser
        getuser = Registrations.objects.filter(username = current_user).first()
        getuser.username = username
        getuser.userimage = userimage
        getuser.passwords = passwords
        getuser.save()
        success = 'user successfuly updated'
        return redirect("/")