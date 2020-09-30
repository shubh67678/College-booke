from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# class AddressField(models.CompositeField):
#     street = models.CharField(max_length=80)
#     city = models.CharField(max_length=80)


# class CollegeField(models.CompositeField):
#     name = models.CharField(max_length=80)
#     address = AddressField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    usermobile = models.CharField(max_length=12, blank=True)
    college_name = models.CharField(max_length=30, default="spit")
    college_address = models.CharField(
        max_length=200, default="andheri,mumbai")

    def __str__(self):
        return f'{self.user.username} Profile'
