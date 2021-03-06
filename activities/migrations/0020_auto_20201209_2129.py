# Generated by Django 3.1.1 on 2020-12-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0019_auto_20201209_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='sport',
            field=models.CharField(choices=[('Running', 'Running'), ('Trail Running', 'Trail Running'), ('Strength Training', 'Strength Training')], default='Running', max_length=75),
        ),
        migrations.AlterField(
            model_name='interval',
            name='heartrate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
