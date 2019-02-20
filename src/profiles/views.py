from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def signup(request):
	context = {}
	template = '/account/signup.html'
	return render(request,template,context)	

def login(request):
	context = {}
	template = '/account/login.html'
	return render(request,template,context)	
