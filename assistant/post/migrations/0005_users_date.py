# Generated by Django 3.0.7 on 2020-08-04 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_users_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date',
            field=models.DateField(auto_now_add=True, default='2020-08-03', verbose_name='Create Date'),
            preserve_default=False,
        ),
    ]