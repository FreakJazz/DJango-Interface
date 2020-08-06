from django.db import models

class GenderChoice(models.TextChoices):
    MALE = u'M', 'Male'
    FEMALE = u'F', 'Female'
    OTHERS = u'O', 'Other'

class Users (models.Model):
    id = models.AutoField(primary_key = True)
    Name = models.CharField('Name', max_length=30, null = False, blank = False)
    Username = models.CharField('Username',max_length=10, null = False, blank = False)
    Phone = models.IntegerField('Phone',null = False, blank = False)
    Email = models.EmailField('Email',null = False, blank = False)
    Password = models.CharField('Password',max_length=10, null = False, blank = False)
    gender = models.CharField('Gener',max_length=2,choices=GenderChoice.choices,default=GenderChoice.OTHERS)
    birthday = models.DateField('Birthday',blank=True,null=True)
    # auto_now = edit every time that the model edit
    # auto_now_add = edit only when you create the model
    date = models.DateField('Create Date', auto_now = False, auto_now_add = True)
    time = models.TimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return "{0},{1}".format(self.Username, self.Password)

class Sign_in (models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField('Username',max_length=10, null = False, blank = False)
    password = models.CharField('Password',max_length=10, null = False, blank = False)
    date = models.DateField('Create Date', auto_now = True, auto_now_add = False)
    time = models.TimeField(auto_now=True, auto_now_add=False)  

    class Meta:
        verbose_name = 'Sign'
        verbose_name_plural = 'Signs'

    def __str__(self):
        return "{0},{1}".format(self.username, self.password)