# Generated by Django 3.1.1 on 2020-12-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activitie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='date',
            field=models.DateField(),
        ),
    ]
