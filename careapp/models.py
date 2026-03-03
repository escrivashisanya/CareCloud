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
    


class MyAppointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=200)    
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) :
        return self.name 



class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"