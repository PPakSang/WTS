# Generated by Django 3.2 on 2021-05-22 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0021_auto_20210522_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='base_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='기준 주차'),
        ),
        migrations.AlterField(
            model_name='student',
            name='changed_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='첫 참여날짜'),
        ),
        migrations.AlterField(
            model_name='student',
            name='day1',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='첫번째 참여일'),
        ),
        migrations.AlterField(
            model_name='student',
            name='day2',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='두번째 참여일'),
        ),
        migrations.AlterField(
            model_name='student',
            name='day3',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='세번째 참여일'),
        ),
        migrations.AlterField(
            model_name='student',
            name='day4',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='네번째 참여일'),
        ),
        migrations.AlterField(
            model_name='student',
            name='plus_day',
            field=models.DateField(default=datetime.datetime(2021, 5, 22, 13, 8, 46, 56369, tzinfo=utc), verbose_name='보너스 참여일'),
        ),
    ]