from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)  # Auto-generated unique ID
    Name = models.CharField(max_length=255)  # Name of the user
    Email = models.EmailField(unique=True)  # Unique email for each user
    Password = models.CharField(max_length=255)  # Hashed password
    Preferences = models.TextField(blank=True, null=True)  # Optional preferences field

    def __str__(self):
        return self.Name

