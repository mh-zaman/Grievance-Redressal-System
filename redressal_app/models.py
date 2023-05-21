from django.db import models

# Create your models here.

# Create your models here.
from datetime import datetime 
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s-%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class StudentModel(models.Model):
    student_id = models.CharField(max_length=13, primary_key=True)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50, unique=True)
    student_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    student_contact = models.CharField(max_length=15)
    student_address = models.CharField(max_length=255)
    student_department = models.CharField(max_length=255)
    student_password = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'student_users'
        
    def isExists(self):
        if StudentModel.objects.filter(student_email=self.student_email):
            return True
        return False

class FacultyModel(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=50)
    faculty_email = models.EmailField(max_length=50, unique=True)
    faculty_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    faculty_contact = models.CharField(max_length=15)
    faculty_address = models.CharField(max_length=255)
    faculty_designation = models.CharField(max_length=255)
    faculty_department = models.CharField(max_length=255)
    faculty_password = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        db_table = 'faculty_users'
        
    def isExists(self):
        if FacultyModel.objects.filter(faculty_email=self.faculty_email):
            return True
        return False
    
class ProctorModel(models.Model):
    proctor_id = models.AutoField(primary_key=True)
    proctor_name = models.CharField(max_length=50)
    proctor_email = models.EmailField(max_length=50, unique=True)
    proctor_image = models.ImageField(upload_to='uploads/', null=True, blank=True) 
    proctor_contact = models.CharField(max_length=15)
    proctor_address = models.CharField(max_length=255)
    proctor_designation = models.CharField(max_length=255)
    proctor_department = models.CharField(max_length=255)
    proctor_password = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        db_table = 'proctor_users'
        
    def isExists(self):
        if ProctorModel.objects.filter(proctor_email=self.proctor_email):
            return True
        return False

class HandlerModel(models.Model):
    handler_id = models.AutoField(primary_key=True)
    handler_name = models.CharField(max_length=25)
    handler_email = models.EmailField(max_length=50, unique=True)
    handler_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    handler_contact = models.CharField(max_length=15)
    handler_address = models.CharField(max_length=255)
    handler_password = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'handler_users'
        
    def isExists(self):
        if HandlerModel.objects.filter(handler_email=self.handler_email):
            return True
        return False
    
class ComplaintModel(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_subject = models.CharField(max_length=255)
    compalint_description = models.CharField(max_length=2555)
    complaint_status = models.CharField(max_length=255)
    complainer_id = models.CharField(max_length=50)
    complainer_name = models.CharField(max_length=50)
    complainer_email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'complaints'