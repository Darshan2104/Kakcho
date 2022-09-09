from django.db import models

# Create your models here.
class MyModel(models.Model):
    upload_csv = models.FileField(upload_to = './' )