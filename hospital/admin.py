from django.contrib import admin

# Register your models here.
#user: asqii
#email: asqii@gmail.com
#password: qwerf123
from .models import Patient, Doctor, Appointment, Department, Service

#admin.site.register(Patient_User)
#admin.site.register(Doctor)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass
