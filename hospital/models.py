import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField()
    iin_num = models.IntegerField(unique=True)
    id_num = models.IntegerField(unique=True)

    bl_groups = [
        ('A', 'Group A'),
        ('B', 'Group B'),
        ('O', 'Group O'),
        ('AB', 'Group AB'),
    ]

    blood_group = models.CharField(max_length=2, choices = bl_groups)
    emergency_cont_num = models.CharField(max_length=15)
    contact_num = models.CharField(max_length=15, unique=True)
    #email = models.EmailField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=150)

    m_status = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]

    marital_status = models.CharField(max_length=7, choices=m_status)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"

class Department(models.Model):
    type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.type

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField()
    iin_num = models.IntegerField(unique=True)
    id_num = models.IntegerField(primary_key=True)
    spec_details_id = models.IntegerField(unique=True)
    experience = models.IntegerField()
    photo = models.ImageField()
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')
    #schedule = models.DateField()
    start_hours = models.TimeField(default=datetime.time(8, 0, 0))
    end_hours = models.TimeField(default=datetime.time(21, 0, 0))

    degrees = [
        ('ASD', 'Associate Degree'),
        ('BA', "Bachelor's Degree"),
        ('MD', "Master's Degree"),
        ('PhD', 'Doctoral Degree'),
    ]

    degree = models.CharField(max_length=3, choices=degrees)
    rating = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    address = models.CharField(max_length=150)
    homepage_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"


class Service(models.Model):
    name = models.CharField(max_length=100, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.TimeField()
    day = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['doctor_id', 'day', 'time'], name='unique_constraint_appointment')
        ]