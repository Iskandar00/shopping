from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import random
from django.contrib import messages
from datetime import timedelta
from django.utils.timezone import now

from apps.users.models import CustomUser, UserAuthCode
from apps.users.services import send_email_to_user


def register(request):
    return render(request, 'register_login/register.html')


def send_code_to_email(request):
    if request.method != 'POST':
        return redirect('register-page')

    email = request.POST.get('email')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')

    if not email:
        messages.error(request, 'email kiritilmadi.')
        return redirect('register-page')

    if not password or not re_password:
        messages.error(request, 'password yoki re_password kiritilmadi.')
        return redirect('register-page')

    if password != re_password:
        messages.error(request, 'parollar bir xil bo\'lishi shart.')
        return redirect('register-page')

    if CustomUser.objects.filter(email=email).last():
        messages.error(request, 'email xato yoki oldin ro\'yxatdan o\'tgan.')
        return redirect('register-page')

    code = random.randint(1000, 10000)
    send_email_to_user(email, code)
    UserAuthCode.objects.create(email=email, code=code, expire_at=now()+timedelta(minutes=5))

    context = {
        'email': email,
        'password': password,
        'code': '',
        'code_error': '',
    }

    return render(request, 'register_login/confirm_email.html', context)


def register_user(request):
    if request.method != 'POST':
        return redirect('register-page')

    email = request.POST.get('email')
    password = request.POST.get('password')
    code = request.POST.get('code')

    UserAuthCode.objects.filter(expire_at__lte=now()).delete()
    object = UserAuthCode.objects.filter(email=email, code=code, expire_at__gte=now())
    if object.last():
        CustomUser.objects.create_user(email=email, password=password)
        object.delete()
    elif UserAuthCode.objects.filter(email=email, expire_at__gte=now()):
        context = {
            'email': email,
            'password': password,
            'code': code,
            'code_error': 'Code not valid.',
        }
        return render(request, 'register_login/confirm_email.html', context)
    else:
        messages.error(request, 'Uzr emailni yoki kodni xato kiritdingiz')
        return redirect('register-page')

    return render(request, 'register_login/login.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email:
            messages.error(request, 'email kiritilmadi.')
            return redirect('login-page')

        if not password:
            messages.error(request, 'password kiritilmadi.')
            return redirect('login-page')

        user = authenticate(request=request, email=email, password=password)

        if not user:
            messages.error(request, 'login yoki parolni notug\'ri kiritdingiz')
            return redirect('login-page')

        login(request, user)
        return redirect('home-page')

    return render(request, 'register_login/login.html')


def log_out(request):
    logout(request)
    return redirect('home-page')
