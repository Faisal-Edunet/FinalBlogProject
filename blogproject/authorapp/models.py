from django.db import models

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.name
