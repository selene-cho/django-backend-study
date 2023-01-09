from django.urls import path 
from .views import Users
# from . import views

urlpatterns = [
    path("", Users.as_view()) # api/v1/users/
]
