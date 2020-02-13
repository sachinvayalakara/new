from django.db import models

# Create your models here.
class Booking(models.Model):
    name   = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    time   = models.TimeField()
    date   = models.DateField()
    vehicle = models.CharField(max_length=15)


class Login(models.Model):
    email  = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25)


class Plan(models.Model):
    plan_title = models.CharField(max_length=30)
    plan_price = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)


class PlanServices(models.Model):
    service_title = models.CharField(max_length=30)
    fk_plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
