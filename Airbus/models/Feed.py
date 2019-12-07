from djongo import models


class Feed(models.Model):
    _id = models.ObjectIdField()
    text = models.TextField()
    user = models.CharField(max_length=20)
    profile_picture = models.TextField()
    full_post = models.TextField()
