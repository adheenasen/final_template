# Generated by Django 3.1.3 on 2022-08-23 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220823_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
    ]
