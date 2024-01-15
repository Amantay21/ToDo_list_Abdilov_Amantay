from django.contrib.auth import get_user_model
from django.db import models


# status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Type(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название типа", unique=True)

    def __str__(self):
        return f'{self.title}'


class Status(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статуса", unique=True)

    def __str__(self):
        return f'{self.title}'


class Task(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.RESTRICT, verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Тип')
    created_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, verbose_name='Проект',
                                related_name='tasks')

    def __str__(self):
        return f'{self.title}'


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=4000, verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата конца')
    users = models.ManyToManyField(get_user_model(), related_name='projects', verbose_name='Пользователи')

    def __str__(self):
        return f'{self.title}'
