# Generated by Django 3.2 on 2021-05-16 00:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0007_auto_20210515_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='changed_day',
            field=models.DateField(default=datetime.date(2021, 5, 16)),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_day',
            field=models.DateField(default=datetime.date(2021, 5, 16)),
        ),
    ]