# Generated by Django 3.1.7 on 2021-02-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0002_blogs_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogers',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogers',
            name='password1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogers',
            name='password2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
