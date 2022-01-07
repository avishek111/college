from django.db import models
from django.core import validators


class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    category_image = models.FileField(upload_to='static/uploads', null=True)

    def __str__(self):
        return self.category_name


class Colleges(models.Model):
    college_name=models.CharField(max_length=500,null=True, validators=[validators.MinLengthValidator(2)])
    college_location=models.CharField(max_length=200,null=True)
    college_level=models.CharField(max_length=200,null=True)
    college_type=models.CharField(max_length=200,null=True)
    college_popularity=models.CharField(max_length=200,null=True)
    college_annual_cost=models.IntegerField()
    college_image = models.FileField(upload_to='static/uploads', null=True)

    def __str__(self):
        return self.college_name


class Locations(models.Model):
    location_name=models.CharField(max_length=200,null=True)
    college_name=models.CharField(max_length=200,null=True)
    stream=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.location_name