# Generated by Django 4.0.4 on 2022-06-03 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certs', '0004_alter_certs_options_alter_certs_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=50, verbose_name='Ф.И.О')),
                ('staff', models.CharField(max_length=100, verbose_name='Должность')),
                ('division', models.CharField(max_length=100, verbose_name='Подразделение')),
                ('gender', models.CharField(max_length=10, verbose_name='Пол')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='certs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='certs.users'),
        ),
    ]
