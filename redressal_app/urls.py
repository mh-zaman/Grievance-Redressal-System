from django.urls import path
from redressal_app import views

urlpatterns = [
    path('', views.home, name="index")
]