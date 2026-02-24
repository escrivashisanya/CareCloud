from django.contrib import admin
from careapp.models import *

# Register your models here.
admin.site.register(patient)

admin.site.register(doctor)

admin.site.register(MyAppointment)