from django.db import models

from django.urls import reverse

# Create your models here.


class School(models.Model):
    Sname = models.CharField(max_length=100)
    Sprincipal = models.CharField(max_length=100)
    Slocation = models.CharField(max_length=100)

    def __str__(self):
        return self.Sname

    def get_absolute_url(self):
        return reverse('School_Detail', kwargs={'pk':self.pk})


class Student(models.Model):
    Stid = models.IntegerField(primary_key=True)
    Stname = models.CharField(max_length=100)
    Stage = models.IntegerField()
    Sname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.Stname

    def get_absolute_url(self):
        return reverse('Student_Detail', kwargs={'pk':self.Stid})

    

