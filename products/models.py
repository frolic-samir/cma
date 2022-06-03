from django.db import models
from customer.models import CustomerProfile

class Tag(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Product(models.Model):
   CHOICE = (
      ('Indoor','Indoor'),
      ('Outdoor','Outdoor')
   )
   name  = models.CharField(max_length=100)
   price = models.DecimalField(decimal_places=2, max_digits=1000)
   category = models.CharField(max_length=100,choices=CHOICE)
   tag = models.ManyToManyField(Tag)
   added_date = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.name

class Order(models.Model):
   STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    )
   customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
   status = models.CharField(max_length=200, blank=True, choices=STATUS)
   created_date = models.DateTimeField(auto_now_add=True)