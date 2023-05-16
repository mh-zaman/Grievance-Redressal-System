from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from redressal_app.models import FacultyModel, StudentModel
# HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, 
# HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseGone, HttpResponseNotModified, 
# HttpResponsePermanentRedirect, HttpResponseTemporaryRedirect, HttpResponseNotModified


# Create your views here.

def navbar_unauthenticated(request):
    return render (request, 'navbar_unauthenticated.html')

def registration_student(request):
    
    if request.method == 'POST':
        
        if request.POST.get('student_name') and request.POST.get('student_email') and  request.POST.get('student_id') and request.POST.get('student_dept') and request.POST.get('student_pass') and request.POST.get('student_repass') :
            saveUser = StudentModel()
            saveUser.student_name = request.POST.get('student_name')
            saveUser.student_email = request.POST.get('student_email')
            saveUser.student_id = request.POST.get('student_id')
            saveUser.student_department = request.POST.get('student_dept')
            
            if request.POST.get('student_pass') == request.POST.get('student_repass'):
                saveUser.student_password = make_password(request.POST.get('student_pass'))
            else:
                messages.error(request, "Passwords do not match")
            
            if saveUser.isExists():
                messages.error(request, request.POST.get('student_name') + " user already registered...! Please Login.")
            else:
                saveUser.save()
                messages.success(request, "Hello " + request.POST.get('student_name') + ", registration details saved successfully...! Please Log in now.")
                
    return render (request, 'registration_student.html')

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

def login_admin(request):
    return render (request, 'login_admin.html')

def login_faculty(request):
    return render (request, 'login_faculty.html')

def login_proctor(request):
    return render (request, 'login_proctor.html')

def login_student(request):
    if request.method == 'POST':
        try:
            userDetail = StudentModel.objects.get(
                student_email=request.POST.get('student_email'))
            if check_password(request.POST.get('student_pass'), (userDetail.student_password)):
                request.session['studnet_email'] = userDetail.student_email
                return redirect('/registration_student/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except StudentModel.DoesNotExist as e:
            messages.error(
                request, 'No user found of this email....!')
    messages.error(
                    request, 'rendering...!')
    return render(request, 'login_student.html')

def complain_faculty(request):
    return render (request, 'complain.html')

def dashboard_student(request):
    
    return render (request, 'dashboard_student.html')