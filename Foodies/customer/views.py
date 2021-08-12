from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
class LoginUser(View):
    def post(self, request, *args, **kwargs):
        try:
            username = request.POST['username']
        except MultiValueDictKeyError:
            username = None
        try:
            password = request.POST['password']
        except MultiValueDictKeyError:
            password = None

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            # messages.success(request, 'User login Successfully!')
            return redirect({'current_url':"{}".format(request.resolver_match.url_name)})

        return render(request, 'customer/login.html')

class UserLogOut(View):
    def get(self, request):
        logout(request)
        return redirect({'current_url':f"{request.resolver_match.url_name}"})
