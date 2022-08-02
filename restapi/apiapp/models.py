from django.db import models

# Create your models here.
class colstudent(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.fname