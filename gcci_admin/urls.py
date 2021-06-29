from django.urls import path
from .views import *

urlpatterns = [
path("",admin_login,name="admin_login"),
path("Dashboard/",admin_homepage,name="admin_homepage"),
]