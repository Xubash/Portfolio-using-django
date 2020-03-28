from django.db import models

class Jobs(models.Model):
    """
    Attributes:
        Image 
        Summary
    """
    image =models.ImageField(upload_to='images/')
    Summary=models.CharField(max_length=200)

