from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=150)
    Email=models.EmailField()
    Marks=models.IntegerField()
    address=models.TextField(null=True,blank=True)
    class Meta:
        db_table='studenlist'


class Teacher(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    Email = models.EmailField()
    address = models.TextField()