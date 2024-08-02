from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import History
from .forms import PostForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def convert_text(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['body']
            html = text.replace('\n', '<br>')
            History.objects.create(user=request.user, text=text, html=html)
            return render(request, 'convert_text.html', {'form': form, 'html': html})
    else:
        form = PostForm()
    return render(request, 'convert_text.html', {'form': form})

@login_required
def history(request):
    histories = History.objects.filter(user=request.user)
    return render(request, 'history.html', {'histories': histories})

@login_required
def delete_history(request, pk):
    history = get_object_or_404(History, pk=pk, user=request.user)
    history.delete()
    return redirect('history')

@login_required
def delete_selected_histories(request):
    if request.method == 'GET' and 'ids' in request.GET:
        ids = request.GET.get('ids').split(',')
        histories = History.objects.filter(user=request.user, id__in=ids)
        histories.delete()
    return redirect('history')







