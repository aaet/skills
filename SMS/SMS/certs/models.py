from django.db import models


class Certs(models.Model):
    exam_name = models.CharField(max_length=50, verbose_name='Наименование экзамена')
    exam_type = models.CharField(max_length=10, verbose_name='Тип экзамена')
    desc = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    doc_pdf = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Документ', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус')
    user = models.ForeignKey('Users', on_delete=models.PROTECT, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['created_at']


class Users(models.Model):
    user = models.CharField(max_length=50, db_index=True, verbose_name='Ф.И.О')
    staff = models.CharField(max_length=100, verbose_name='Должность')
    division = models.CharField(max_length=100, verbose_name='Подразделение')
    gender = models.CharField(max_length=10, verbose_name='Пол')
    birthday = models.DateField(blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['user']
