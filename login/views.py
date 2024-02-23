from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import regiterForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def registration(request):
    if request.method == 'POST':
        form=regiterForm (request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
           
    else:
        form=regiterForm()
    return render(request, 'registration.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
           
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')  
    else:
        form = AuthenticationForm()
    return render(request, './userlogin.html', {'form': form})
            
def profile(request):
    if request.user.is_authenticated:
        return render(request, './profile.html',{'user':request.user})
    else:
        return redirect('userlogin')

def user_logout(request):
    logout(request)
    return redirect('userlogin')
        
          
   
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request, './changepassword.html', {'form': form})
    else:
        return redirect('userlogin')