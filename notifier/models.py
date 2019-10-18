from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserComment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.user.username


# Registering UserComment model to admin panel
admin.site.register(UserComment)