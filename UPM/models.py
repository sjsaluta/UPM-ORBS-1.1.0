from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name