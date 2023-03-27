from django.urls import path
from redressal_app import views

urlpatterns = [
    path('', views.navbar_unauthenticated, name="navbar_unauthenticated"),
    path('login_admin/', views.login_admin, name="login_admin"),
    path('login_faculty/', views.login_faculty, name="login_faculty"),
    path('login_proctor/', views.login_proctor, name="login_proctor"),
    path('login_student/', views.login_student, name="login_student"),
]