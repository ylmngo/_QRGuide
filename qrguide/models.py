from django.db import models 

class Comments(models.Model): 
    name = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self): 
        return self.name 
