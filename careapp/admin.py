from django.contrib import admin
from careapp.models import patient
from careapp.models import doctor
# Register your models here.
admin.site.register(patient)

admin.site.register(doctor)