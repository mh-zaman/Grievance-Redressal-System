from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.db import connection
from django.template.loader import get_template

from xhtml2pdf import pisa

from redressal_app.models import ComplaintModel, FacultyModel, HandlerModel, ProctorModel, StudentModel
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
    
    if request.method == 'POST':
        try:
            userDetail = FacultyModel.objects.get(faculty_email=request.POST.get('faculty_email'))
            if check_password(request.POST.get('faculty_password'), userDetail.faculty_password):
                request.session['email'] = userDetail.faculty_email
                return redirect('/profile_faculty/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except FacultyModel.DoesNotExist as e:
            messages.error(request, 'No user found of this email....!')    
    return render (request, 'login_faculty.html')

def login_handler(request):
    if request.method == 'POST':
        try:
            userDetail = HandlerModel.objects.get(handler_email=request.POST.get('handler_email'))
            print(check_password(request.POST.get('handler_password'), userDetail.handler_password))
            if check_password(request.POST.get('handler_password'), userDetail.handler_password):
                request.session['email'] = userDetail.handler_email
                return redirect('/dashboard_handler/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except HandlerModel.DoesNotExist as e:
            messages.error(request, 'No user found of this email....!')    
    return render (request, 'login_handler.html')

def login_proctor(request):
    if request.method == 'POST':
        try:
            userDetail = ProctorModel.objects.get(proctor_email=request.POST.get('proctor_email'))
            print(check_password(request.POST.get('proctor_password'), userDetail.proctor_password))
            if check_password(request.POST.get('proctor_password'), userDetail.proctor_password):
                request.session['email'] = userDetail.proctor_email
                return redirect('/dashboard_proctor/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except ProctorModel.DoesNotExist as e:
            messages.error(request, 'No user found of this email....!')    
    return render (request, 'login_proctor.html')

def login_student(request):
    if request.method == 'POST':
        try:
            userDetail = StudentModel.objects.get(student_email=request.POST.get('student_email'))
            if check_password(request.POST.get('student_password'), userDetail.student_password):
                request.session['email'] = userDetail.student_email
                return redirect('/profile_student/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except StudentModel.DoesNotExist as e:
            messages.error(request, 'No user found of this email....!')                
    return render (request, 'login_student.html')

def registration_faculty(request): 
    if request.method == 'POST':   
        if request.POST.get('faculty_name') and request.POST.get('faculty_email') and request.POST.get('faculty_dept') and request.POST.get('faculty_designation') and request.POST.get('faculty_pass') and request.POST.get('faculty_repass') :
            saveUser = FacultyModel()
            saveUser.faculty_name = request.POST.get('faculty_name')
            saveUser.faculty_email = request.POST.get('faculty_email')
            saveUser.faculty_department = request.POST.get('faculty_dept')
            saveUser.faculty_designation = request.POST.get('faculty_designation')
            if len(request.FILES) != 0:
                saveUser.faculty_image = request.FILES['faculty_image']   
            if request.POST.get('faculty_pass') != request.POST.get('faculty_repass'):
                messages.error(request, "Passwords do not match")
            else:
                saveUser.faculty_password = make_password(request.POST.get('faculty_pass'))
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
            if len(request.FILES) != 0:
                saveUser.student_image = request.FILES['image_student']
            
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
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        return render(request, 'navbar_student.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_student.html')

def dashboard_student(request):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        return render(request, 'dashboard_student.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_student.html')

def complain_previous_student(request):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM `complaints` WHERE `complainer_id` = %s ORDER BY `complaint_id` ASC;', [user.student_id])
        complaints = cursor.fetchall()
        cursor.close()
        return render(request, 'complain_previous_student.html', {'user': user, 'complaints' : complaints})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_student')

def complain_new_student(request):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        if request.method == 'POST':
            if request.POST.get('subject') and request.POST.get('complaint'):
                sub = request.POST.get('subject')
                comp = request.POST.get('complaint')
                saveComplain = ComplaintModel()
                saveComplain.complaint_subject = sub
                saveComplain.compalint_description = comp
                saveComplain.complaint_status = 'Pending'
                saveComplain.complainer_id = user.student_id
                saveComplain.complainer_name = user.student_name
                saveComplain.complainer_email = user.student_email
                saveComplain.save()
                messages.success(request, "Complaint saved successfully...!")
        return render(request, 'complain_new_student.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_student')

def profile_student(request):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        return render(request, 'profile_student.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_student')

def edit_profile_student(request):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        if request.method == 'POST':
            user.student_name = request.POST.get('student_name')
            user.student_email = request.POST.get('student_email')
            user.student_department = request.POST.get('student_department')
            user.student_contact = request.POST.get('student_contact')
            user.student_address = request.POST.get('student_address')
            if len(request.FILES) != 0:
                user.student_image = request.FILES['image_student']
            user.save()
            messages.success(request, "Profile updated successfully...!")
        return render(request, 'edit_profile_student.html', {'user': user})
        
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_student')            

def change_password_student(request):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        if request.method == 'POST':
            if check_password(request.POST.get('current_password'), user.student_password):
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                if new_password != confirm_password:
                    messages.error(request, 'Passwords do not match')
                else:
                    user.student_password = make_password(new_password)
                    user.save()
                    messages.success(request, "Password changed successfully...!")
            else:
                messages.error(request, 'Current password is incorrect')
                return render(request, 'change_password_student.html', {'user': user})
        return render(request, 'change_password_student.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_student.html')

def logout(request):
    try:
        del request.session['email']
        messages.success(request, "Successfully logged out.")
    except:
        messages.error(request, "An error occurred. Try again.")
        return redirect('/')
    return redirect('/')

def pdf_generated_student(request, token):
    try:
        user = StudentModel.objects.get(student_email=request.session['email'])
        try:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM complaints WHERE complaint_id = %s;', [token])
            complaints = cursor.fetchall()
            cursor.close()
            template_path = 'pdf_generated_student.html'
            context = {'user': user, 'complaint': complaints[0]}

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="complaint.pdf"'
            template = get_template(template_path)
            html = template.render(context)
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except:
            messages.error(request, 'You have no pdf to show.')
            return redirect('/')
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_student')





#------------------------------------------------------------------------------------------------------------------------------------------





def navbar_faculty(request):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        return render(request, 'navbar_faculty.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_faculty.html')


def dashboard_faculty(request):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        return render(request, 'dashboard_faculty.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_faculty.html')

def complain_previous_faculty(request):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM `complaints` WHERE `complainer_id` = %s ORDER BY `complaint_id` ASC;', [user.faculty_id])
        complaints = cursor.fetchall()
        cursor.close()
        
        return render(request, 'complain_previous_faculty.html', {'user': user, 'complaints' : complaints})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_faculty')


def complain_new_faculty(request):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        if request.method == 'POST':
            if request.POST.get('subject') and request.POST.get('complaint'):
                sub = request.POST.get('subject')
                comp = request.POST.get('complaint')
                saveComplain = ComplaintModel()
                saveComplain.complaint_subject = sub
                saveComplain.compalint_description = comp
                saveComplain.complaint_status = 'Pending'
                saveComplain.complainer_id = user.faculty_id
                saveComplain.complainer_name = user.faculty_name
                saveComplain.complainer_email = user.faculty_email
                
                saveComplain.save()
                messages.success(request, "Complaint saved successfully...!")
        return render(request, 'complain_new_faculty.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_faculty')


def profile_faculty(request):
    
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        return render(request, 'profile_faculty.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_faculty')


def edit_profile_faculty(request):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        if request.method == 'POST':
            user.faculty_name = request.POST.get('faculty_name')
            user.faculty_email = request.POST.get('faculty_email')
            user.faculty_department = request.POST.get('faculty_department')
            user.faculty_contact = request.POST.get('faculty_contact')
            user.faculty_address = request.POST.get('faculty_address')
            if len(request.FILES) != 0:
                user.faculty_image = request.FILES['image_faculty']
            user.save()
            messages.success(request, "Profile updated successfully...!")
        return render(request, 'edit_profile_faculty.html', {'user': user})
        
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_faculty')  

def change_password_faculty(request):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        if request.method == 'POST':
            if check_password(request.POST.get('current_password'), user.faculty_password):
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                if new_password != confirm_password:
                    messages.error(request, 'Passwords do not match')
                else:
                    user.faculty_password = make_password(new_password)
                    user.save()
                    messages.success(request, "Password changed successfully...!")
            else:
                messages.error(request, 'Current password is incorrect')
                return render(request, 'change_password_faculty.html', {'user': user})
        return render(request, 'change_password_faculty.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_faculty.html')


def pdf_generated_faculty(request, token):
    try:
        user = FacultyModel.objects.get(faculty_email=request.session['email'])
        try:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM complaints WHERE complaint_id = %s;', [token])
            complaints = cursor.fetchall()
            cursor.close()
            template_path = 'pdf_generated.html'
            context = {'user': user, 'complaint': complaints[0]}

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="complaint.pdf"'
            template = get_template(template_path)
            html = template.render(context)
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except:
            messages.error(request, 'You have no pdf to show.')
            return redirect('/')
    except:
        messages.error(request, 'You need to login first')
        return redirect('login_faculty')



#------------------------------------------------------------------------------------------------------------------------------------------



def navbar_handler(request):
    try:
        user = HandlerModel.objects.get(handler_email=request.session['email'])
        return render(request, 'navbar_faculty.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return render (request, 'login_handler.html')



def dashboard_handler(request):
    return render (request, 'dashboard_handler.html')


def complain_all(request):
    return render (request, 'complain_all.html')


def profile_handler(request):
    #print('Session Email: ')
    #print(email)
    #return render (request, 'profile_handler.html' , {'email': email})
    return render (request, 'profile_handler.html')


def edit_profile_handler(request):
    return render (request, 'edit_profile_handler.html')

def change_password_handler(request):
    return render (request, 'change_password_handler.html')









#------------------------------------------------------------------------------------------------------------------------------------------

def complain_faculty(request):
    return render (request, 'complain.html')




def home_handler(request):
    return render (request, 'home_handler.html')





def profile_proctor(request):
    return render (request, 'profile_proctor.html')

def profile_handler(request):
    return render (request, 'profile_handler.html')






def dashboard_proctor(request):
    return render (request, 'dashboard_proctor.html')

def paste(request):
    return render (request, 'paste.html')