import uuid

from django.contrib.auth.models import User
from django.db import models


class Airport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    runways = models.IntegerField()


class UserDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    role = models.CharField(max_length=10)


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_id = models.CharField(max_length=20)
    flight_name = models.CharField(max_length=30)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    airlines = models.CharField(max_length=10)
    total_seats_economy = models.IntegerField()
    vacant_seats_economy = models.IntegerField()
    total_seats_business = models.IntegerField()
    vacant_seats_business = models.IntegerField()
    price_economy = models.FloatField()
    price_business = models.FloatField()
    date = models.DateField()
