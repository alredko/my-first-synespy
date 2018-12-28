from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=1)
    progress = models.CharField(max_length=10)
    created_date = models.DateTimeField('date created')
