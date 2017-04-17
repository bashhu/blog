from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import permission_required


def accounts(request):
    return render(request,"login.html",{})

@permission_required('article.add_article',login_url='/users/')
def user_list(request):
    user_list=User.objects.all()
    return render(request, "user_list.html", {'user_list':user_list})

def user_logout(request):
    logout(request)
    return redirect('/')


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    print request.user.is_authenticated()
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        print user.is_active
        if user.is_active:
            print user
            res = "User is valid, active and authenticated"
            login(request,user)
        else:
            res = "The password is valid, but the account has been disabled!"
            return render(request, "login.html", {})
    else:
        # the authentication system was unable to verify the username and password
        res = "The username and password were incorrect."
        return render(request, "login.html", {})
    return render(request,"login_res.html",{'res': res})