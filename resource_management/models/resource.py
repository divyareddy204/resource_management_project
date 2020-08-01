from django.db import models

class Resource(models.Model):

    resource_name = models.CharField(max_length=50, unique=True)
    resource_link = models.CharField(max_length=50)
    resource_service = models.CharField(max_length=50)
    resource_pic_url = models.URLField(max_length=50)
    description = models.CharField(max_length=50)
