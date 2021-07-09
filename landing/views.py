from django.shortcuts import render
from django.http import HttpResponse
from gcci_admin.models import Contact
from random import randint
from GCCI.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string
from gcci_admin.models import Events, Testimonials
 

def home(request):
	return render(request, 'home.html')


def news(request):
	context = {}
	news = Events.objects.filter(types="News")
	context['data'] = news
	return render(request, 'news.html',context)


def newsfull(request):
	return render(request, 'newsfull.html')


def services(request):
	return render(request, 'services.html')



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

	if request.method == 'POST':

		if request.POST['submit'] == 'client':
  #    		 
			name = request.POST['name']
			designation = request.POST['designation']
			company = request.POST['companyname']
			review = request.POST['review']
			photo = request.FILES['photo']


			try:

				user = Testimonials()
				user.status = "Pending"
				user.types = "Users"
				user.photo = photo
				user.name = name
				user.designation = designation
				user.company = company
				user.review = review

				user.save()

			except Exception as e:
				print(e)
			else:
				pass

		if request.POST['submit'] == 'organization':
  #    		 
			name = request.POST['name']
			designation = request.POST['designation']
			company = request.POST['companyname']
			review = request.POST['review']
			photo = request.FILES['photo']


			try:

				user = Testimonials()
				user.status = "Pending"
				user.types = "Company"
				user.photo = photo
				user.name = name
				user.designation = designation
				user.company = company
				user.review = review

				user.save()

			except Exception as e:
				print(e)
			else:
				pass
			

	return render(request, "testimonials.html")


def contactus(request):

	def random_with_N_digits(n):
		range_start = 10**(n-1)
		range_end = (10**n)-1
		return randint(range_start, range_end)

	if request.method == 'POST':
		salulation = request.POST['salutation']
		fname = request.POST['fname']
		mname = request.POST['mname']
		lname = request.POST['lname']
		designation = request.POST['designation']
		company = request.POST['company']
		company_location = request.POST['company_location']
		email = request.POST['email']
		phone = request.POST['phone']
		industry_type = request.POST['industry_type']
		interested_in = request.POST['interest']
		source = request.POST['source']
		enquiry = request.POST['enquiry']

		try:
			user = Contact()

			user.salutation = salulation
			user.first_name = fname
			user.middle_name = mname
			user.last_name = lname
			user.designation = designation
			user.company = company
			user.company_location = company_location
			user.email = email
			user.phone = phone
			user.industry_type = industry_type
			user.interested_in = interested_in
			user.source = source
			user.created_date = enquiry

			user.save()
			subject = "Enquiry"
			message = enquiry
			send_mail(subject, message, EMAIL_HOST_USER, [email])

			context['success'] = "Success"
			return render(request, "contactus.html",context)

		except Exception as e:
			print(e)

		else:
			context['failed'] = "Failed"
			return render(request, "contactus.html",context)

	

	return render(request, "contactus.html")
