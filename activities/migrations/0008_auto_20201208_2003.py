# Generated by Django 3.1.1 on 2020-12-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20201208_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='date',
            field=models.DateField(),
        ),
    ]
