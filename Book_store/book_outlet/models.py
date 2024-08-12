from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    slug = models.SlugField(default="",null=False,db_index=True)
    title = models.CharField(max_length=50)
    rate = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)])
    author = models.CharField(null=True,max_length=50)
    is_bestselling= models.BooleanField(default=False)
    description = models.TextField()  # New description field
    image=models.ImageField(upload_to='book_cover/',null=True,blank=True)
    
    def save(self,*args, **kwargs):
        self.slug=slugify( self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):  
	    return f"{self.title} ({self.rate}) {self.author}  {self.is_bestselling}"
 
    