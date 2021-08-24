from django.db import models
# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    nationality=models.CharField(max_length=12)
    Student_id=models.CharField(max_length=12)
    image_of_the_student=models.ImageField(upload_to="register_student")
    email=models.EmailField(max_length=20)
    #gender_choice=[('f','female'),('m','male'),('o','other')]
    gender=models.CharField(max_length=12)
    subject=models.CharField(max_length=14)
    health_records=models.FileField(max_length=200)
    classroom=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=12)
    admission_date=models.DateField()
    parent_contact=models.DateField()
    academic_year=models.DateField(max_length=8)
    #langauage_choices=[('E','English'),('K','Kiswahili')('F','French)')]
    language=models.CharField(max_length=15)
    profile_pic=models.ImageField(upload_to="images/")
    laptop_serial_number=models.CharField(max_length=30,null=True,blank=True)
