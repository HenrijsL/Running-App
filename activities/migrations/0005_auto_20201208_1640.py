# Generated by Django 3.1.1 on 2020-12-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20201208_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
