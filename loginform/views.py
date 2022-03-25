from django.shortcuts import render,redirect
from signupforms.models import Registrations

# Create your views here.
def login_users(request):
    errors = ''
    if request.method == 'POST':
        username = request.POST['usernames']
        password = request.POST['password']
        #getuser
        getuser = Registrations.objects.filter(username=username)
        if getuser.exists():
            getuser = Registrations.objects.get(username=username)
            if getuser.passwords == password:
                response = redirect("/home/")
                response.set_cookie("logedinuser",username)
                return response
            else:
                errors = 'Wrong password, check and try again.'
        else:
            errors = 'user with this username dont exist'
    context = {
        'title':'music player Login',
        'errors':errors
    }
    return render(request, "login.html", context)