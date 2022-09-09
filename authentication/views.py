from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    
    return render(request, 'index.html')

def register(request):

    if request.method == 'POST':
        forms = UserCreationForm(request.POST)

        if forms.is_valid():
            forms.save()
            messages.success(request, "Registered Successfully")
        # else:
        #     messages.error(request, "Could not validate credentials")
            return redirect("register")
    else:
        forms = UserCreationForm()
        
    context = {
        'forms': forms,
       
    }

    return render(request, 'authentication/register.html', context)

def user_login(request):
    forms = UserLoginForm()
    if request.method == "POST":
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                if 'next' in request.path:
                    return redirect(request.get['next'])
                return redirect("booker-home")
                
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("login")

    context = {
        "forms": forms
    }
    return render(request, "authentication/login.html", context)

@login_required
def user_logout(request):

    logout(request)
    return redirect('login')

@login_required()
def change_password(request):
    
    

    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password CHanged Succssfully")
            return redirect('change_password')

        else:
            messages.error(request, 'Please correct the error below.')
    
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form
    }

    return render(request, 'authentication/change_password.html', context)