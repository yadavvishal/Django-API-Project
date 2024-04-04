from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Paragraph(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"Paragraph {self.pk}"
