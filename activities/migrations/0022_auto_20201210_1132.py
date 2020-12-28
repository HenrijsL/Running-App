# Generated by Django 3.1.1 on 2020-12-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0021_auto_20201210_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='heartrate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interval',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]