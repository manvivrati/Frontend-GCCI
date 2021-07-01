from django.urls import path, include
from .views import *

urlpatterns = [

path('', home, name="home"),
path('Services/', services, name="services"),
path('Contact_us/', contact_us, name="contact_us"),
path('Services/Lean_Manufacturing', lean_manufacturing, name="lean_manufacturing"),
path('Services/Smart_Factory_IoT', smart_factory, name="smart_factory"),
path('Services/TPM', tpm, name="tpm"),
path('Services/Innovation_Management', innovation_management, name="innovation_management"),
path('Services/Service_and_Sales', services_and_sales, name="services_and_sales"),
path('Services/Organization_and_HR', organization_and_hr, name="organization_and_hr"),
path('Training/Training_for_Manufacture', training_for_manufacture, name="training_for_manufacture"),
path('Training/P-Course', p_course, name="p_course"),
path('Training/Kart_Factory', kart_factory, name="kart_factory"),
path('News/', news, name="news"),
path('Newsfull/', newsfull, name="newsfull"),
path('Manufacturing/', manufacturing, name="manufacturing"),
path('Achievements/', achievements, name='achievements'),
path('AboutGCCI/', AboutGCCI, name="AboutGCCI"),
path('environment/', environment, name="Environment"),
path('education/', education, name="Education"),
path('spirituality/', spirituality, name="Spirituality"),
path('culture/', culture, name="Culture"),
path('testimonials/', testimonials, name="Testimonials"),

]