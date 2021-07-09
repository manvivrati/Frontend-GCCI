from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Events
# Create your views here. 


def admin_homepage(request):
	return render(request, 'admin_dashboard.html')


def admin_login(request):
	return render(request, 'admin_login.html')

def add_events(request):

	context = {}
	

	if request.method == "POST":
		title = request.POST['title']
		details = request.POST['details']
		date = request.POST['date']
		link = request.POST['link']
		# for videos in request.FILES:
		# 	videos = request.FILES['videos']

		print(title,details,date)

		try:

			events = Events()

			events.types = "Event"
			events.title = title
			events.description = details
			events.event_date = date
			events.link = link


			events.save()

			context['success'] = "Added Successfully"
			return render(request, 'add_events.html',context)

		except Exception as e:

			print(e)

		else:

			context['failed'] = "Failed !"
			return render(request, 'add_events.html',context)
	return render(request, 'add_events.html')

def manage_events(request):

	context = {}
	events = Events.objects.all()
	context['data'] = events
	return render(request, 'manage_events.html',context)

def add_news(request):

	context = {}
	

	if request.method == "POST":
		title = request.POST['title']
		details = request.POST['details']
		date = request.POST['date']
		# for videos in request.FILES:
		# 	videos = request.FILES['videos']

		print(title,details,date)

		try:

			news = Events()

			news.types = "News"
			news.title = title
			news.description = details
			news.event_date = date

			news.save()

			context['success'] = "Added Successfully"
			return render(request, 'add_news.html',context)

		except Exception as e:

			print(e)

		else:

			context['failed'] = "Failed !"
			return render(request, 'add_news.html',context)

	return render(request, 'add_news.html')

def manage_news(request):
	context = {}
	news = Events.objects.all()
	context['data'] = news
	return render(request, 'manage_news.html',context)

	return render(request, 'manage_news.html')


def add_blogs(request):

	context = {}
	

	if request.method == "POST":
		title = request.POST['title']
		details = request.POST['details']
		# for videos in request.FILES:
		# 	videos = request.FILES['videos']
		author = request.POST['author']


		print(title,details,author)

		try:

			blog = Blog()

			blog.title = title
			blog.description = details
			blog.author = author

			blog.save()

			context['success'] = "Added Successfully"
			return render(request, 'add_blog.html',context)

		except Exception as e:

			print(e)

		else:

			context['failed'] = "Failed !"
			return render(request, 'add_blog.html',context)

	return render(request, 'add_blog.html')

def manage_blogs(request):
	context = {}
	blogs = Blog.objects.all()
	context['data'] = blogs
	return render(request, 'manage_blog.html',context)
	return render(request, 'manage_blog.html')


def summary(request):
	return render(request,'dashboard.html')