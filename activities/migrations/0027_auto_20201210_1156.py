# Generated by Django 3.1.1 on 2020-12-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0026_auto_20201210_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(blank=True, choices=[('', ''), ('Easy Run', 'Easy Run'), ('Marathon Pace', 'Marathon Pace'), ('Tempo', 'Tempo'), ('Interval', 'Interval'), ('Repetition', 'Repetition'), ('Progressive', 'Progressive'), ('Warm Up', 'Warm Up'), ('Cool Down', 'Cool Down'), ('Rest', 'Rest'), ('Jog', 'Jog')], max_length=75),
        ),
        migrations.AlterField(
            model_name='interval',
            name='type',
            field=models.CharField(choices=[('', ''), ('Easy Run', 'Easy Run'), ('Marathon Pace', 'Marathon Pace'), ('Tempo', 'Tempo'), ('Interval', 'Interval'), ('Repetition', 'Repetition'), ('Progressive', 'Progressive'), ('Warm Up', 'Warm Up'), ('Cool Down', 'Cool Down'), ('Rest', 'Rest'), ('Jog', 'Jog')], max_length=75),
        ),
    ]