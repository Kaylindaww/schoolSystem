from django.db import models
# Create your models here.
class Courses(models.Model):
 courses_name = models.CharField(max_length=20)
courses_Trainer = models.CharField(max_length=20)
courses_course_code=models.CharField(max_length=20)
courses_description=models.CharField(max_length=20)
