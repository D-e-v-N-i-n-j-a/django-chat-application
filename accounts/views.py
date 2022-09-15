from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('chat')
        else:
            print('something went wrong')
            return redirect('login')
            
    return render(request,'login.html')



def logout(request):
    auth.logout(request)
    print('user successfully logout')
    return redirect('login')



