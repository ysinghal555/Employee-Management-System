from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone_number = models.TextField(max_length=10)

    def __str__(self):
        return "{0}".format(self.name)
