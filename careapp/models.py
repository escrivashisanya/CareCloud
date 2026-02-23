from django.db import models

# Create your models here.
class patient(models.Model) :
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered = models.DateTimeField()
    medicalhistory = models.TextField()


    def __str__(self) :
        return self.firstname + " " +self.lastname
    


class doctor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20) 
    specialisation = models.CharField(max_length=200) 
    phonenumber = models.CharField(max_length=10)  
    email = models.EmailField()
    yearsofexperience = models.IntegerField()
    DOB = models.DateField(null=True)
    age = models.IntegerField(null=True)

    def __str__(self) :
        return self.firstname + " " +self.lastname