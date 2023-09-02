from django.db import models 

class Comments(models.Model): 
    name = models.CharField(max_length=64) 
    department = models.CharField(max_length=64) 
    phone = models.CharField(max_length=12) 
    message = models.TextField() 

    def __str__(self): 
        return f"Message by {self.name}" 
