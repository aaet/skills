# Generated by Django 4.0.4 on 2022-06-01 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certs',
            old_name='disc',
            new_name='desc',
        ),
    ]
