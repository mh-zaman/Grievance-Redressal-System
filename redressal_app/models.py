from django.db import models

# Create your models here.

from datetime import datetime
import os


def filePathStudents(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s-%s" % (timeNow, old_filename)
    return os.path.join('students/', filename)

def filePathFaculties(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s-%s" % (timeNow, old_filename)
    return os.path.join('faculties/', filename)

def filePathProctor(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s-%s" % (timeNow, old_filename)
    return os.path.join('proctors/', filename)

def filePathAdmins(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s-%s" % (timeNow, old_filename)
    return os.path.join('admins/', filename)

class StudentModel(models.Model):
    student_id = models.CharField(max_length=13, primary_key=True)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50, unique=True)
    student_image = models.ImageField(upload_to='students/', null=True, blank=True)
    student_contact = models.CharField(max_length=11)
    student_address = models.CharField(max_length=255)
    student_department = models.CharField(max_length=255)
    student_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'student_users'
        
    def isExists(self):
        if StudentModel.objects.filter(student_email=self.student_email):
            return True
        return False

class FacultyModel(models.Model):
    faculty_name = models.CharField(max_length=50)
    faculty_email = models.EmailField(max_length=50, unique=True)
    faculty_image = models.ImageField(upload_to='faculties/', null=True, blank=True)
    faculty_contact = models.CharField(max_length=11)
    faculty_address = models.CharField(max_length=255)
    faculty_designation = models.CharField(max_length=255)
    faculty_department = models.CharField(max_length=255)
    faculty_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'faculty_users'
        
    def isExists(self):
        if FacultyModel.objects.filter(faculty_email=self.faculty_email):
            return True
        return False
    
class ProctorModel(models.Model):
    proctor_id = models.CharField(max_length=13, primary_key=True)
    proctor_name = models.CharField(max_length=50)
    proctor_email = models.EmailField(max_length=50, unique=True)
    proctor_image = models.ImageField(upload_to='proctors/', null=True, blank=True)
    proctor_contact = models.CharField(max_length=11)
    proctor_address = models.CharField(max_length=255)
    proctor_designation = models.CharField(max_length=255)
    proctor_department = models.CharField(max_length=255)
    proctor_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'proctor_users'
        
    def isExists(self):
        if ProctorModel.objects.filter(proctor_email=self.proctor_email):
            return True
        return False

class AdminModel(models.Model):
    admin_id = models.CharField(max_length=13, primary_key=True)
    admin_name = models.CharField(max_length=25)
    admin_email = models.EmailField(max_length=50, unique=True)
    admin_image = models.ImageField(upload_to='admins/', null=True, blank=True)
    admin_contact = models.CharField(max_length=11)
    admin_address = models.CharField(max_length=255)
    admin_designation = models.CharField(max_length=255)
    admin_department = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'admin_users'
        
    def isExists(self):
        if AdminModel.objects.filter(admin_email=self.admin_email):
            return True
        return False
    
class ComplaintModel(models.Model): 
    compalint_id = models.AutoField(primary_key=True)
    complaint_subject = models.CharField(max_length=255)
    compalint_description = models.TextField()
    compalint_status = models.CharField(max_length=255)
    complaint_progress = models.CharField(max_length=255)
    complaint_total = models.IntegerField()
    compalint_resolved = models.IntegerField()
    complaint_pending = models.IntegerField()
    complaint_raised = models.IntegerField()
    complainer_id = models.CharField(max_length=13)
    complainer_name = models.CharField(max_length=50)
    complainer_email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'complaints'