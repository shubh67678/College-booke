from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class friends(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, name="to-user")
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, name="from-user")
    time_stamp = models.TimeField(auto_now_add=True)
