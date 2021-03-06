from django.db import models
from django import forms

class Courses(models.Model):
    coursename = models.CharField(max_length=100)

    def __str__(self):
        return str(self.coursename)

class Members(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    studentID = models.CharField(max_length=8)
    subject = models.ForeignKey('Courses', on_delete=models.CASCADE)
    year = models.CharField(max_length=1)

    def __str__(self):
        return str(self.firstname)
