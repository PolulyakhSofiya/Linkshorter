from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#
#
class Login(View):
    print('Login_View')
    template_name = 'ShortLinks/Auth/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print('LoginPOST')
        print(request.GET.get('next'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request.GET.get('next'))
        return render(request, self.template_name, {'error': 'No such user or password is wrong. Please try again.'})


def logout_view(request):
    logout(request)
    return redirect('ShortLinks:home')
