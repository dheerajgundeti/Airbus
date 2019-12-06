import uuid
from django.db import models


class Airport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    runways = models.IntegerField()
