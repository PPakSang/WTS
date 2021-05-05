# Generated by Django 3.2 on 2021-05-05 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ForeignkeyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.choose')),
            ],
        ),
    ]
