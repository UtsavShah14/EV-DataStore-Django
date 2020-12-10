from django.db import models

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=50)
    vehicle_manufacturer = models.CharField(max_length=50)
    vehicle_year = models.IntegerField()
    vehicle_battery_size = models.IntegerField()
    vehicle_WLTP_range = models.IntegerField()
    vehicle_cost = models.IntegerField()
    vehicle_power = models.IntegerField()

class User(models.Model):
    user_name = models.CharField(max_length=25)
