from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'pet_search/home.html')


def about_us(request):
    return render(request, 'pet_search/about_us.html')


def lost(request):
    return render(request, 'pet_search/lost.html')


def detected(request):
    return render(request, 'pet_search/detected.html')

#
# def login(request):
#     return render(request, 'registration/login.html')


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с єтим адресом уже зарегестрирован!')
        else:
            if form.is_valid():
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password, email=email)
                ins.email = email
                ins.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно заресестрировались')
                return redirect('/')


    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)