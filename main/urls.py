from django.urls import path
from . import views  # Импортируем ваши view-функции
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('shop/', views.shop, name='shop'),  # Страница магазина
    path('contact/', views.contact, name='contact'),  # Контакты
    path('single/', views.single, name='single'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),  # Ваша функция регистрации
    # После выхода переходим на главную
]
