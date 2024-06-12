from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class CustomUser(AbstractUser):
    description = models.CharField(max_length=200, null = True,blank = True)
    def __str__(self):
        return self.username

class Banner(models.Model):
    """banner model"""
    uuid = models.UUIDField(primary_key=True,default= uuid.uuid4)
    name = models.CharField(max_length=500)

    image = models.ImageField(upload_to='category_images',null = True, blank = True)
    description = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.name
    
    class Meta:
        """meta class"""
        verbose_name = 'Custom Banner Name'  # Customize the singular name
        verbose_name_plural = 'Custom Banner Names'
 
# Create your models here.
