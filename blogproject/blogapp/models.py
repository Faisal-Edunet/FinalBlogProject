from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey('authorapp.Author', on_delete=models.CASCADE)
    published_date = models.DateTimeField(null=True, blank=True)
