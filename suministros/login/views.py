from django.shortcuts import render
from .models import Login
from .forms import LoginForm
from django.http import HttpResponse

def login(request):

    if request.method == 'POST':
        login = Login()
        login.username = request.POST['username']
        login.password = request.POST['password']
        form = LoginForm()

        if validateUser(login):
            context = {
                'accessLevel': Login.objects.get(username=login.username).accessLevel,
            }
            return render(request, 'index.html', context)
        
        return render(request, 'login/login.html', {'form': form})
        
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})

def validateUser(login):
    for user in Login.objects.values_list('username','password'):
        if user[0] == login.username:
            if user[1] == login.password:
                return True
    return False
