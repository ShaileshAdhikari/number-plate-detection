# Generated by Django 4.0.2 on 2022-02-13 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_numberplate_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberplate',
            name='Added',
        ),
    ]
