from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'home.html')


def news(request):
	return render(request, 'news.html')


def newsfull(request):
	return render(request, 'newsfull.html')


def services(request):
	return render(request, 'services.html')


def contact_us(request):
	return HttpResponse('Contact Us')


def lean_manufacturing(request):
	return render(request, 'Lean_Manufacture.html')


def smart_factory(request):
	return render(request, 'smartfactory.html')


def tpm(request):
	return HttpResponse('Home Page')


def innovation_management(request):
	return render(request, 'Innovation_Management.html')


def services_and_sales(request):
	return render(request, 'SalesAndInnovation.html')


def organization_and_hr(request):
	return render(request, 'organization_hr.html')


def training_for_manufacture(request):
	return render(request, 'manufacture_page.html')


def p_course(request):
	return render(request, 'pcourse.html')


def kart_factory(request):
	return render(request, 'kartfactory.html')


def manufacturing(request):
	return render(request, 'manufacturing.html')


def achievements(request):
	return render(request, 'achievements.html')


def AboutGCCI(request):
	return render(request, 'aboutus.html')


def environment(request):
	return render(request, "environment.html")


def education(request):
	return render(request, "education.html")


def spirituality(request):
	return render(request, "spirituality.html")


def culture(request):
	return render(request, "culture.html")


def testimonials(request):
	return render(request, "testimonials.html")


def contactus(request):
	return render(request, "contactus.html")
