from django.urls import path
from redressal_app import views

urlpatterns = [
    
    path('navbar_unauthenticated/', views.navbar_unauthenticated, name="navbar_unauthenticated"),
    path('', views.startup_page, name="startup_page"),
    path('home_unauth/', views.home_unauth, name="home_unauth"),
    path('about_unauth/', views.about_unauth, name="about_unauth"),
    path('login_faculty/', views.login_faculty, name="login_faculty"),
    path('login_handler/', views.login_handler, name="login_handler"),
    path('login_proctor/', views.login_proctor, name="login_proctor"),
    path('login_student/', views.login_student, name="login_student"),
    path('registration_faculty/', views.registration_faculty, name="registration_faculty"),
    path('registration_student/', views.registration_student, name="registration_student"),
    path('logout/', views.logout, name="logout"),
    
    path('delete_complaint/<token>/', views.delete_complaint, name='delete_complaint'),
    path('action_complaint/', views.action_complaint, name='action_complaint'),
    
    path('delete_complaint_proctor/<token>/', views.delete_complaint_proctor, name='delete_complaint_proctor'),
    path('action_complaint_proctor/', views.action_complaint_proctor, name='action_complaint_proctor'),
    
    
    
    
    path('navbar_student/', views.navbar_student, name="navbar_student"),
    path('dashboard_student/', views.dashboard_student, name="dashboard_student"),
    path('complain_previous_student/', views.complain_previous_student, name="complain_previous_student"),
    path('complain_new_student/', views.complain_new_student, name="complain_new_student"),
    path('profile_student/', views.profile_student, name="profile_student"), 
    path('edit_profile_student/', views.edit_profile_student, name="edit_profile_student"),
    path("change_password_student/", views.change_password_student, name="change_password_student"),
    path('pdf_generated_student/<token>/', views.pdf_generated_student, name='pdf_generated_student'),
    
    
    path('navbar_faculty/', views.navbar_faculty, name="navbar_faculty"),
    path('dashboard_faculty/', views.dashboard_faculty, name="dashboard_faculty"),
    path('complain_previous_faculty/', views.complain_previous_faculty, name="complain_previous_faculty"),
    path('complain_new_faculty/', views.complain_new_faculty, name="complain_new_faculty"),
    path('profile_faculty/', views.profile_faculty, name="profile_faculty"),
    path('edit_profile_faculty/', views.edit_profile_faculty, name="edit_profile_faculty"),
    path("change_password_faculty/", views.change_password_faculty, name="change_password_faculty"),
    path('pdf_generated_faculty/<token>/', views.pdf_generated_faculty, name='pdf_generated_faculty'),
    
    
    
    
    
    path('navbar_handler/', views.navbar_handler, name="navbar_handler"), 
    path('dashboard_handler/', views.dashboard_handler, name="dashboard_handler"),
    path('complain_all/', views.complain_all, name="complain_all"),
    path('profile_handler/', views.profile_handler, name="profile_handler"),
    path('edit_profile_handler/', views.edit_profile_handler, name="edit_profile_handler"),
    path("change_password_handler/", views.change_password_handler, name="change_password_handler"),
    
    
    path('navbar_proctor/', views.navbar_proctor, name="navbar_proctor"),
    path('dashboard_proctor/', views.dashboard_proctor, name="dashboard_proctor"),
    path('complain_all_proctor/', views.complain_all_proctor, name="complain_all_proctor"),
    path('profile_proctor/', views.profile_proctor, name="profile_proctor"),
    path('edit_profile_proctor/', views.edit_profile_proctor, name="edit_profile_proctor"),
    path("change_password_proctor/", views.change_password_proctor, name="change_password_proctor"),
    path('pdf_generated_proctor/<token>/', views.pdf_generated_proctor, name='pdf_generated_proctor'),
]