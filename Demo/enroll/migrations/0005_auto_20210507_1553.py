# Generated by Django 3.2 on 2021-05-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_alter_student_first_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fixed_day',
            field=models.CharField(choices=[('월요일', '월요일'), ('화요일', '화요일'), ('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일'), ('토요일', '토요일'), ('일요일', '일요일')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_new',
            field=models.CharField(choices=[('신규', '신규'), ('재등록', '재등록')], default='o', max_length=5),
        ),
    ]