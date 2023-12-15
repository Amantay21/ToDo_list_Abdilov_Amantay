from django.db import models

# status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Type(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название типа", unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.id}. {self.title}'


class Status(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статуса", unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.id}. {self.title}'

class Task(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ManyToManyField('webapp.Type', related_name='types', blank=True)
    created_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Время обновления', auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
