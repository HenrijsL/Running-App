# Generated by Django 3.1.1 on 2020-12-09 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0012_auto_20201209_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='time',
            new_name='duration',
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('Easy Run', 'Easy Run'), ('Marathon Pace', 'Marathon Pace'), ('Tempo', 'Tempo'), ('Interval', 'Interval'), ('Repetition', 'Repetition'), ('Progressive', 'Progressive'), ('Warm Up', 'Warm Up'), ('Cool Down', 'Cool Down'), ('Rest', 'Rest'), ('Jog', 'Jog')], max_length=75),
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Easy Run', 'Easy Run'), ('Marathon Pace', 'Marathon Pace'), ('Tempo', 'Tempo'), ('Interval', 'Interval'), ('Repetition', 'Repetition'), ('Progressive', 'Progressive'), ('Warm Up', 'Warm Up'), ('Cool Down', 'Cool Down'), ('Rest', 'Rest'), ('Jog', 'Jog')], max_length=75)),
                ('distance', models.FloatField()),
                ('duration', models.DurationField()),
                ('heartrate', models.IntegerField(null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
            ],
        ),
    ]
