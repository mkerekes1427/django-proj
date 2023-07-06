from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Observation(models.Model):

    person = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    date = models.DateField(null=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    category = models.CharField(null=False, blank=False, max_length=255)
    picture = models.ImageField(upload_to="", default="profile.jpeg", 
                                null=False, blank=False)
    description = models.TextField(null=True, blank=True, max_length=1000)
    color = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.person} {self.name}'




