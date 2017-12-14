from django.db import models
from datetime import date, datetime

class Student(models.Model):
	firstname = models.CharField(max_length = 50)
	lastname = models.CharField(max_length = 50)
	age = models.IntegerField()
	phone_number = models.IntegerField()
	major = models.CharField(max_length = 100)


