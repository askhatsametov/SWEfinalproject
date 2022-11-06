from django.contrib import admin

# Register your models here.
#user: asqii
#email: asqii@gmail.com
#password: qwerf123
from .models import Patient, Doctor

#admin.site.register(Patient_User)
#admin.site.register(Doctor)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass
