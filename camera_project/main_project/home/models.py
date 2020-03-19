from django.db import models
from django.core.validators import MaxValueValidator

class Add_camera(models.Model):
    name = models.CharField(max_length=30)
    make = models.CharField(max_length=20)
    camera_model = models.CharField(max_length=30)
    zoom = models.IntegerField()
    ip = models.GenericIPAddressField (null=False)


    def __str__(self):
        return self.name


class Company_register(models.Model):
    #company_id = models.PositiveIntegerField()
    company_name = models.CharField(max_length=100)
    password_first = models.CharField(max_length=50)
    password_second = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Batch(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to="images/")

    def __str__(self):
        return self.name


class Person_Entry(models.Model):
    choice = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100,choices = choice)
    image1 = models.ImageField(upload_to='image/')
    image2 = models.ImageField(upload_to='image/')
    image3 = models.ImageField(upload_to='image/')
    image4 = models.ImageField(upload_to='image/')
    image5 = models.ImageField(upload_to='image/')
    image6 = models.ImageField(upload_to='image/')
    image7 = models.ImageField(upload_to='image/')
    image8 = models.ImageField(upload_to='image/')


