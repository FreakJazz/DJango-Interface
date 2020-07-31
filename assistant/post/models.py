from django.db import models

class Users (models.Model):
    Name = models.CharField(max_length=30)
    Username = models.CharField(max_length=10)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=10)

    def __str__(self):
        return self.Phone
        