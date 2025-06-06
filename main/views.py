from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html')  # Главная страница

def shop(request):
    return render(request, 'shop.html')  # Магазин

def about(request):
    return render(request, 'about.html')  # Контакты

def contact(request):
    return render(request, 'contact.html')

def single(request):
    return render(request, 'shop-single.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} успешно создан! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})