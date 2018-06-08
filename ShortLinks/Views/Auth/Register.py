from django.db import IntegrityError
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class Register(View):
    print('Login_View')
    template_name = 'ShortLinks/Auth/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print('RegisterPOST')
        print(request.GET.get('next'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        newUser = User(username=username)
        try:
            newUser.save()
        except IntegrityError:
            return render(request, self.template_name, {'error': 'Account Exists'})
        newUser.set_password(password)
        newUser.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
        return render(request, self.template_name, {'error': 'No such user or password is wrong. Please try again.'})
