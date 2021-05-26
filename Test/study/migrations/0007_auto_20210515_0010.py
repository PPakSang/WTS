# Generated by Django 3.2 on 2021-05-14 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_alter_student_first_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.CharField(blank=True, choices=[('왕초급', '왕초급'), ('초급', '초급'), ('중급', '중급')], max_length=3),
        ),
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 0, 10, 48, 26902)),
        ),
    ]
