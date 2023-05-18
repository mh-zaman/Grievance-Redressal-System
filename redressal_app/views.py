from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import Argon2PasswordHasher

from redressal_app.models import FacultyModel, StudentModel
# HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, 
# HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseGone, HttpResponseNotModified, 
# HttpResponsePermanentRedirect, HttpResponseTemporaryRedirect, HttpResponseNotModified


# Create your views here.

def navbar_unauthenticated(request):
    return render (request, 'navbar_unauthenticated.html')

def home_unauth(request):
    return render (request, 'home_unauth.html')

def about_unauth(request):
    return render (request, 'about_unauth.html')

def login_faculty(request):
    return render (request, 'login_faculty.html')

def login_handler(request):
    return render (request, 'login_handler.html')

def login_proctor(request):
    return render (request, 'login_proctor.html')

def login_student(request):
    if request.method == 'POST':
        try:
            userDetail = StudentModel.objects.get(student_email=request.POST.get('student_email'))
            if check_password(request.POST.get('student_password'), userDetail.student_password):
                request.session['email'] = userDetail.student_email
                return redirect('/dashboard_student/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except StudentModel.DoesNotExist as e:
            messages.error(request, 'No user found of this email....!')
                    
    return render (request, 'login_student.html')

def registration_faculty(request):
    
    if request.method == 'POST':
        
        if request.POST.get('faculty_name') and request.POST.get('faculty_email') and request.POST.get('faculty_dept') and request.POST.get('faculty_designtion') and request.POST.get('faculty_pass') and request.POST.get('faculty_repass') :
            saveUser = FacultyModel()
            saveUser.faculty_name = request.POST.get('faculty_name')
            saveUser.faculty_email = request.POST.get('faculty_email')
            saveUser.faculty_department = request.POST.get('faculty_dept')
            saveUser.faculty_designation = request.POST.get('faculty_designtion')
            
            if request.POST.get('faculty_pass') == request.POST.get('faculty_repass'):
                saveUser.faculty_password = make_password(request.POST.get('faculty_pass'))
            else:
                messages.error(request, "Passwords do not match")
                return render(request, "registration_faculty.html")
            
            if saveUser.isExists():
                messages.error(request, request.POST.get('faculty_name') + " user already registered...! Please Login.")
            else:
                saveUser.save()
                messages.success(request, "Hello " + request.POST.get('faculty_name') + ", registration details saved successfully...! Please Log in now.")
    
    return render (request, 'registration_faculty.html')

def registration_student(request):
    
    if request.method == 'POST':
        
        if request.POST.get('student_name') and request.POST.get('student_email') and  request.POST.get('student_id') and request.POST.get('student_dept') and request.POST.get('student_pass') and request.POST.get('student_repass') :
            saveUser = StudentModel()
            saveUser.student_name = request.POST.get('student_name')
            saveUser.student_email = request.POST.get('student_email')
            saveUser.student_id = request.POST.get('student_id')
            saveUser.student_department = request.POST.get('student_dept')
            
            if request.POST.get('student_pass') != request.POST.get('student_repass'):
                messages.error(request, "Passwords do not match")
            else:
                saveUser.student_password = make_password(request.POST.get('student_pass'))
                
                if saveUser.isExists():
                    messages.error(request, request.POST.get('student_name') + " user already registered...! Please Login.")
                else:
                    saveUser.save()
                    messages.success(request, "Hello " + request.POST.get('student_name') + ", registration details saved successfully...! Please Log in now.")
                    
    return render (request, 'registration_student.html')



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def navbar_student(request):
    return render (request, 'navbar_student.html')

def dashboard_student(request):
    return render (request, 'dashboard_student.html')

def complain_previous_student(request):
    return render (request, 'complain_previous_student.html')

def complain_new_student(request):
    return render (request, 'complain_new_student.html')

def profile_student(request):
    #print('Session Email: ')
    #print(email)
    #return render (request, 'profile_student.html' , {'email': email})
    return render (request, 'profile_student.html')

def edit_profile_student(request):
    return render (request, 'edit_profile_student.html')

def change_password_student(request):
    return render (request, 'change_password_student.html')




#------------------------------------------------------------------------------------------------------------------------------------------





def navbar_faculty(request):
    return render (request, 'navbar_faculty.html')


def dashboard_faculty(request):
    return render (request, 'dashboard_faculty.html')


def complain_previous_faculty(request):
    return render (request, 'complain_previous_faculty.html')


def complain_new_faculty(request):
    return render (request, 'complain_new_faculty.html')


def profile_faculty(request):
    #print('Session Email: ')
    #print(email)
    #return render (request, 'profile_faculty.html' , {'email': email})
    return render (request, 'profile_faculty.html')


def edit_profile_faculty(request):
    return render (request, 'edit_profile_faculty.html')

def change_password_faculty(request):
    return render (request, 'change_password_faculty.html')






#------------------------------------------------------------------------------------------------------------------------------------------



def navbar_handler(request):
    return render (request, 'navbar_handler.html')


def dashboard_handler(request):
    return render (request, 'dashboard_handler.html')


def complain_all(request):
    return render (request, 'complain_all.html')











#------------------------------------------------------------------------------------------------------------------------------------------

def complain_faculty(request):
    return render (request, 'complain.html')




def home_handler(request):
    return render (request, 'home_handler.html')





def profile_proctor(request):
    return render (request, 'profile_proctor.html')

def profile_handler(request):
    return render (request, 'profile_handler.html')






def complain_dashboard(request):
    return render (request, 'complain_dashboard.html')

def paste(request):
    return render (request, 'paste.html')