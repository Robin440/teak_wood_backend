from django.db import models

# Create your models here.
import uuid

class Banner(models.Model):
    """model for banner"""
    uuid = models.UUIDField(primary_key= True, default=uuid.uuid4)
    name = models.CharField(max_length=500, null=True, blank = True)

    description = models.TextField(null= True,blank = True)
    image = models.ImageField(upload_to="banner_images",null = True, blank = True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name if self.name else "Unnamed"
        