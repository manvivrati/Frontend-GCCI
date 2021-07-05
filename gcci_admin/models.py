from django.db import models

# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length=100,help_text="Enter Your First Name")
	middle_name = models.CharField(max_length=100,help_text="Enter Your Middle Name")
	last_name = models.CharField(max_length=100,help_text="Enter Your Last Name")
	designation = models.CharField(max_length=50)
	company = models.CharField(max_length=100)
	company_location = models.TextField()
	email = models.EmailField(max_length=100)
	phone = models.BigIntegerField()
	industry_type_choices = (('default 1','deafult 1'),('default 2','deafult 2'),('default 3','deafult 3'))
	industry_type = models.CharField(max_length=100,choices=industry_type_choices)
	interseted_in_choices = (('default 1','deafult 1'),('default 2','deafult 2'),('default 3','deafult 3'))
	interested_in = models.CharField(max_length=100,choices=interseted_in_choices)
	source_choices = (('default 1','deafult 1'),('default 2','deafult 2'),('default 3','deafult 3'))
	source = models.CharField(max_length=100,choices=source_choices)
	enquiry = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)


	class Meta:
		db_table = "Contact Us"

	def __str__(self):
		return self.first_name+" "+self.middle_name+" "+self.last_name


class Contact_Popup(models.Model):
	name = models.CharField(max_length=200)
	designation = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	location = models.TextField()
	mobile = models.BigIntegerField()
	email = models.EmailField(max_length=100)
	enquiry = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "Contact Popup"

	def __str__(self):
		return self.name

class Testimonials(models.Model):
	types_choices = (('Users','Users'),('Company','Company'))
	types = models.CharField(max_length=100,choices=types_choices)
	name = models.CharField(max_length=200)
	designation = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='Testimonials/')
	review = models.TextField()
	status_choices = (('Accepted','Accepted'),('Pending','Pending'),('Rejected','Rejected'))
	status = models.CharField(max_length=100,choices=status_choices)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "Testimonials"

	def __str__(self):
		return self.name+self.company

class Events(models.Model):
	type_choice = (('News','News'),('Event','Event'))
	types = models.CharField(max_length=100,choices=type_choice)
	title = models.CharField(max_length=100)
	description = models.TextField()
	event_date = models.DateTimeField()
	registered_member = models.IntegerField(null=True)
	link = models.CharField(max_length=255,null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "Events"

	def __str__(self):
		return self.title+" "+ self.type


class Blog(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	video_url = models.JSONField(null=True)
	author = models.CharField(max_length=100)

	class Meta:
		db_table = "Blogs"

	def __str__(self):
		return self.title


class Event_Images(models.Model):
	event = models.ForeignKey(Events, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='Events/Images/')
	uploaded_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "Events Images"



class Blog_Images(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='Blogs/Images/')
	uploaded_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "Blog Images"



	
