from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'home.html')

def services(request):
	return HttpResponse('Services Page')

def contact_us(request):
	return HttpResponse('Contact Us Page')

def lean_manufacturing(request):
	return HttpResponse('Lean Manufacturing Page')

def smart_factory(request):
	return HttpResponse('Home Page')

def tpm(request):
	return HttpResponse('Home Page')


def innovation_management(request):
	return HttpResponse('Home Page')


def services_and_sales(request):
	return HttpResponse('Home Page')


def organization_and_hr(request):
	return HttpResponse('Home Page')

def training_for_manufacture(request):
	pass

def p_course(request):
	pass

def kart_factory(request):
	pass