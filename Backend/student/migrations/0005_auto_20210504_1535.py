# Generated by Django 3.2 on 2021-05-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_test_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='check',
        ),
        migrations.AddField(
            model_name='test',
            name='enroll',
            field=models.CharField(choices=[('o', '참'), ('x', '불')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
