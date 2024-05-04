from django.db import models

# Create your models here.
import uuid


class Category(models.Model):
    uuid = models.UUIDField(primary_key= True,default= uuid.uuid4)
    name = models.CharField(max_length=500, null= True,blank = True)
    description = models.TextField(null=True, blank = True)
    image = models.ImageField(upload_to='category_images',null = True, blank = True)
    def __str__(self):
        return self.name if self.name else "Unnamed"

class Subcategory(models.Model):
    uuid = models.UUIDField(primary_key= True,default= uuid.uuid4)
    name = models.CharField(max_length=500, null= True,blank = True)
    description = models.TextField(null=True, blank = True)
    image = models.ImageField(upload_to='category_images',null = True, blank = True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null = True, blank = True)
    def __str__(self):
        return self.name if self.name else "Unnamed"

class SubofSub(models.Model):
    uuid = models.UUIDField(primary_key= True,default= uuid.uuid4)
    name = models.CharField(max_length=500, null= True,blank = True)
    description = models.TextField(null=True, blank = True)
    image = models.ImageField(upload_to='category_images',null = True, blank = True)
    sub_category = models.ForeignKey(Subcategory,on_delete=models.SET_NULL,null = True, blank = True)
    def __str__(self):
        return self.name if self.name else "Unnamed"

class Product(models.Model):
    uuid = models.UUIDField(primary_key= True,default= uuid.uuid4)
    name = models.CharField(max_length=500, null= True,blank = True)
    description = models.TextField(null=True, blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    qty = models.IntegerField(default=0)
    image_one = models.ImageField(upload_to='product_images',null = True, blank = True)
    image_two = models.ImageField(upload_to='product_images',null = True, blank = True)
    image_three = models.ImageField(upload_to='product_images',null = True, blank = True)
    image_four = models.ImageField(upload_to='product_images',null = True, blank = True)
    image_five = models.ImageField(upload_to='product_images',null = True, blank = True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null = True, blank = True)
    def __str__(self):
        return self.name if self.name else "Unnamed"

