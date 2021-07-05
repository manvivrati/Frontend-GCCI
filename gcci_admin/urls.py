from django.urls import path
from .views import *

urlpatterns = [
path("", admin_login, name="admin_login"),
path("Dashboard/", admin_homepage, name="admin_homepage"),
path("Dashboard/Add_Events", add_events, name="add_events"),
path("Dashboard/Manage_Events", manage_events, name="manage_events"),
path("Dashboard/Add_News", add_news, name="add_news"),
path("Dashboard/Manage_News", manage_news, name="manage_news"),
path("Dashboard/Add_Blogs", add_blogs, name="add_blogs"),
path("Dashboard/Manage_Blogs", manage_blogs, name="manage_blogs"),
path("Dashboard/Summary", summary, name="summary"),

]
