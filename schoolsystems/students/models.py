from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
