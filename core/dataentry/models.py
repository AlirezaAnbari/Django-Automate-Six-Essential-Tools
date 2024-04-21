from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    def ___str__(self):
        return self.name
    
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    
    def ___str__(self):
        return self.customer_name