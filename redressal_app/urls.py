from django.urls import path
from redressal_app import views

urlpatterns = [
    path('', views.navbar_unauthenticated, name="navbar_unauthenticated"),
    path('login_admin/', views.login_admin, name="login_admin"),
    path('login_faculty/', views.login_faculty, name="login_faculty"),
    path('login_proctor/', views.login_proctor, name="login_proctor"),
    path('login_student/', views.login_student, name="login_student"),
    path('registration_student/', views.registration_student, name="registration_student"),
    path('registration_faculty/', views.registration_faculty, name="registration_faculty"),
    path('complain/', views.complain_faculty, name="complain"),
    path('dashboard_student/', views.dashboard_student, name="dashboard_student"),
]