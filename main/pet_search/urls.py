from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('lost', views.lost, name='lost'),
    path('detected', views.detected, name='detected'),
    path('about_us', views.about_us, name='about_us'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

]
