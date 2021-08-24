from django.db.models.fields import CharField, TimeField
from schoolsystems import events
from django.db import models
# Create your models here.
class Events(models.Model):
    events_name=models.CharField()
    events_location=models.CharField()
    events_start_time=models.TimeField()
    events_end_time=models.TimeField()
    events_describtion=models.CharField()

    

