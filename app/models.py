from django.db import models
from django.urls import reverse

# Create your models here.


class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('School_detail',kwargs={'pk':self.pk})
    

class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=100)
    sid=models.IntegerField()