# Generated by Django 3.2 on 2021-05-16 00:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0009_auto_20210516_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='changed_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 16, 0, 26, 14, 536522, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 16, 9, 26, 14, 536522)),
        ),
    ]