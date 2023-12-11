from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name