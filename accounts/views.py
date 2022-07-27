from django.shortcuts import redirect, render
from django.contrib import auth
# Create your views here.

def login(request):
    # Handle with Login once POST request recieved.
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username = userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')


    # to show login.html that has login form once GET request recieved.
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')