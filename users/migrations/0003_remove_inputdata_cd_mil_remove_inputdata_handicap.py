# Generated by Django 4.2.16 on 2025-03-08 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_inputdata_alter_userregistrationmodel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputdata',
            name='CD_MIL',
        ),
        migrations.RemoveField(
            model_name='inputdata',
            name='Handicap',
        ),
    ]
