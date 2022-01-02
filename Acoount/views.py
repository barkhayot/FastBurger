from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def registerUser(request):
    if request.user.is_authenticated:
        return redirect('food_menu')
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully has been created')
            return redirect('loginUser')
    context = {
        'form': form
    }
    return render(request, 'account/registerUser.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('food_menu')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('food_menu')
        else:
            messages.info(request, 'Username or Password is incorrect')

    
    return render(request, 'account/loginUser.html')

@login_required(login_url='loginUser')
def logoutUser(request):
    logout(request)
    return redirect('loginUser')