# Generated by Django 3.2 on 2021-05-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210506_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_day',
            field=models.DateField(),
        ),
    ]