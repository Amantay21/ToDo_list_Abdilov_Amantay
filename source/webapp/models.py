from django.db import models


class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, default='Новая', verbose_name="Статус")
    date_of_completion = models.DateTimeField(verbose_name='Дата выполнения', auto_now_add=False, null=False, blank=False)


    def __str__(self):
        return f'{self.id}. {self.description}'
