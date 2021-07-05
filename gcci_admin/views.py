from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 


def admin_homepage(request):
	return render(request, 'admin_dashboard.html')


def admin_login(request):
	return render(request, 'admin_login.html')

def add_events(request):
	return render(request, 'add_events.html')

def manage_events(request):
	return render(request, 'manage_events.html')

def add_news(request):
	return render(request, 'add_news.html')

def manage_news(request):
	return render(request, 'manage_news.html')


def add_blogs(request):
	return render(request, 'add_blog.html')

def manage_blogs(request):
	return render(request, 'manage_blog.html')


def summary(request):
	return render(request,'dashboard.html')