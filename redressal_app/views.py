from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, 
# HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseGone, HttpResponseNotModified, 
# HttpResponsePermanentRedirect, HttpResponseTemporaryRedirect, HttpResponseNotModified


# Create your views here.

def navbar_unauthenticated(request):
    return render (request, 'navbar_unauthenticated.html')

def login_admin(request):
    return render (request, 'login_admin.html')

def login_faculty(request):
    return render (request, 'login_faculty.html')

def login_proctor(request):
    return render (request, 'login_proctor.html')

def login_student(request):
    return render (request, 'login_student.html')

def registration(request):
    return render (request, 'registration.html')
