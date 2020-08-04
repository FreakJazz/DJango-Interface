from django.db import models

class Users (models.Model):
    id = models.AutoField(primary_key = True)
    Name = models.CharField('Name', max_length=30, null = False, blank = False)
    Username = models.CharField('Username',max_length=10, null = False, blank = False)
    Phone = models.IntegerField('Phone',null = False, blank = False)
    Email = models.EmailField('Email',null = False, blank = False)
    Password = models.CharField(max_length=10, null = False, blank = False)
    #date = models.DateField('Create Date', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return "{0},{1}".format(self.Username, self.Password)
        