# Generated by Django 3.2 on 2021-05-16 00:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0012_auto_20210516_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='study',
        ),
        migrations.AlterField(
            model_name='student',
            name='changed_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 16, 0, 31, 17, 253242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 16, 0, 31, 17, 253242, tzinfo=utc)),
        ),
    ]