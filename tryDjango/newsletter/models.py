from django.conf.app_template import models
from django.db import models

# Create your models here.
class Signup(models.Model):
    email=models.EmailField(max_length=120)
    full_name=models.CharField(default='default_name',blank=True,max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

