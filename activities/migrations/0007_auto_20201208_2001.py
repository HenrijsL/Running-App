# Generated by Django 3.1.1 on 2020-12-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20201208_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
