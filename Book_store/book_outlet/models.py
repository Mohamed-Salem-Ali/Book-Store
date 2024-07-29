from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rate = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)])
    is_bestselling= models.BooleanField()
    
    def __str__(self):  
	    return f"{self.title} ({self.rate})"