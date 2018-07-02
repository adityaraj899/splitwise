from django.shortcuts import render, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


def index(request):
    return render(request, 'account/index.html')
'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'
'''

@login_required
def profile(request) :
    return render(request, 'account/profile.html')


@login_required
def dashboard(request) :
    return render(request, 'account/dashboard.html')

@login_required
def about(request) :
    return render(request, 'account/about.html')

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('user_login') # to redirect to views on success
    template_name = 'account/signup.html'


@csrf_protect
def user_login(request):
    #context_dict = {}
	if request.method == "POST":
		user = authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return render(request,'account/login.html', {'login_fail': True})
	else:
		return render(request, 'account/login.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/")
