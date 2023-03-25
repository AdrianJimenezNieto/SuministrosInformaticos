from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from django.http import HttpResponse

def signUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    if request.method == 'GET':
        form = RegisterForm()
    return render(request, 'registration/signUp.html', {'form': form})

