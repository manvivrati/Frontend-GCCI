from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def admin_homepage(request):
	return render(request, 'admin_dashboard.html')
def admin_login(request):
	return render(request, 'admin_login.html')