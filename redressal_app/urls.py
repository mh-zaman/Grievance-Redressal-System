from django.urls import path
from redressal_app import views

urlpatterns = [
    #path('', views.home, name="index"),
    path('', views.navbar_home, name="navbar_home"),
]