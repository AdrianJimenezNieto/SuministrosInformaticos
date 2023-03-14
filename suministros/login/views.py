from django.shortcuts import render
from .models import Login
from .forms import LoginForm
from django.http import HttpResponse

def login(request):

    if request.method == 'POST':
        login = Login()
        login.username = request.POST['username']
        login.password = request.POST['password']

        if validateUser(login):
            context = {
                'accessLevel': Login.objects.get(username=login.username).accessLevel,
            }
            return HttpResponse('login correcto ->' + str(context['accessLevel']))
        
        return HttpResponse('login fallido')
        
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})

def validateUser(login):
    for user in Login.objects.values_list('username'):
        if user[0] == login.username:
            return True
    return False
