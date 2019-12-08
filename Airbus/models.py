import uuid

from django.contrib.auth.models import User
from django.db import models
from djongo import models as dmodels


class Feed(dmodels.Model):
    _id = dmodels.ObjectIdField()
    text = dmodels.TextField()
    user = dmodels.CharField(max_length=20)
    profile_picture = dmodels.TextField()
    full_post = dmodels.TextField()

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
    flight_id = models.CharField(max_length=20)
    flight_name = models.CharField(max_length=30)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    airlines = models.CharField(max_length=10)
    total_seats_economy = models.IntegerField()
    vacant_seats_economy = models.IntegerField()
    total_seats_business = models.IntegerField()
    vacant_seats_business = models.IntegerField()
    price_economy = models.IntegerField()
    price_business = models.IntegerField()
    date = models.DateField()

class Coupon(dmodels.Model):
    coupon_id = dmodels.CharField(max_length=20)
    coupon_code = dmodels.CharField(max_length=10)
    coupon_description = dmodels.CharField(max_length=10)


class Bookings(models.Model):
    flight_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    flight_name = models.CharField(max_length=30)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    airlines = models.CharField(max_length=10)
    price_economy = models.IntegerField()