# Generated by Django 3.0.7 on 2020-08-04 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_users_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date',
        ),
    ]
