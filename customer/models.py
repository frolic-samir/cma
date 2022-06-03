from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   name = models.CharField(max_length=200, null=True)
   email = models.EmailField()
   contact = models.CharField(max_length=15)
   profile_pic = models.ImageField(null=True,blank=True)
   created_date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name