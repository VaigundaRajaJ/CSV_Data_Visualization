from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import FileUploadForm
from .models import UploadedFile
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signin_view')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'upload_file.html')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required(login_url='signin')
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    render(request, 'upload_file.html', {'form': form})

@login_required(login_url='signin')
def file_list(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})

@login_required(login_url='signin')
def signout_view(request):
    logout(request)
    return redirect('signin')


# Create your views here.
