import uuid
from django.db import models


class UserDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
