from django.contrib import messages
from django.views import View
from Airbus.models import *
from django.shortcuts import *
from Airbus.forms.airforms import *
from django.urls import resolve
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def homepage(request):
    return render(request,template_name='homepage.html',context={'title':'Airbus'})


class loginuser(View):
    def get(self,request):
        if(request.user.is_authenticated):
            return redirect('flights_html')
        login_form=loginn()
        return render(request,template_name='login.html',context={'form':login_form,'title':'Login User'})
    def post(self,request):
        user=request.POST['username']
        passw=request.POST['password']
        user = authenticate(username=user, password=passw)
        if user is not None:
            login(request,user)
            return redirect('flights_html')
        else:
            messages.error(request,'Invalid-credentials')
            return redirect('login_html')

class Signupuser(View):
    def get(self,request):
        signup_form=signup()
        return  render(request,template_name='signup.html',context={'form':signup_form,'title':'SignUp User'})
    def post(self,request):
        form=signup(request.POST)
        if(form.is_valid()):
            user= User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('login_html')

def logout_user(request):
    logout(request)
    return redirect('login_html')