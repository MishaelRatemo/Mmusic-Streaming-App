from django.shortcuts import render,redirect
from signupforms.models import Registrations
# Create your views here.
def user_register(request):
    errors = ''
    if request.method == 'POST':
        username = request.POST['usernames']
        userimage = request.FILES['userimage']
        passwords = request.POST['password']
        roles = request.POST['roles']
        # getuser
        getuser = Registrations.objects.filter(username = username)
        if getuser.exists():
            errors = 'sorry user with this username already exist'
        else:
            newuser = Registrations(username=username,userimage = userimage, passwords=passwords,roles = roles)
            newuser.save()
            return redirect('/')
    context = {
        'title':'music player signup',
        'errors':errors
    }
    return render(request, "signup.html", context)