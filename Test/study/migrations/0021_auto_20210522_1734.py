# Generated by Django 3.2 on 2021-05-22 08:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0020_auto_20210522_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='first_day',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fourth_day',
        ),
        migrations.RemoveField(
            model_name='student',
            name='second_day',
        ),
        migrations.RemoveField(
            model_name='student',
            name='third_day',
        ),
        migrations.AddField(
            model_name='student',
            name='day1',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 8, 34, 3, 251727, tzinfo=utc), verbose_name='첫번째 참여일'),
        ),
        migrations.AddField(
            model_name='student',
            name='day2',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 8, 34, 3, 251727, tzinfo=utc), verbose_name='두번째 참여일'),
        ),
        migrations.AddField(
            model_name='student',
            name='day3',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 8, 34, 3, 251727, tzinfo=utc), verbose_name='세번째 참여일'),
        ),
        migrations.AddField(
            model_name='student',
            name='day4',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 8, 34, 3, 251727, tzinfo=utc), verbose_name='네번째 참여일'),
        ),
        migrations.AlterField(
            model_name='student',
            name='changed_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 8, 34, 3, 251727, tzinfo=utc), verbose_name='첫 참여날짜'),
        ),
        migrations.AlterField(
            model_name='student',
            name='plus_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 8, 34, 3, 251727, tzinfo=utc), verbose_name='보너스 참여일'),
        ),
    ]