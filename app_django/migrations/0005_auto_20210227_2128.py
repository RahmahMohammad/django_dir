# Generated by Django 3.1.7 on 2021-02-27 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0004_blogers_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blogers',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='blogers',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='blogers',
            name='username',
        ),
    ]
