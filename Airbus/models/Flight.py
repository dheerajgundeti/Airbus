import uuid
from django.db import models

from . import Airport


class Flight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_id = models.CharField(max_length=20)
    flight_name = models.CharField(max_length=30)
    source = models.ForeignKey(Airport, on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE)
    airlines = models.CharField(max_length=10)
    total_seats_economy = models.IntegerField()
    vacant_seats_economy = models.IntegerField()
    total_seats_business = models.IntegerField()
    vacant_seats_business = models.IntegerField()
    price_economy = models.FloatField()
    price_business = models.FloatField()
