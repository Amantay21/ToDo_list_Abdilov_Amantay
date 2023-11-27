from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, default='Новая', verbose_name="Статус", choices=status_choices)
    date_of_completion = models.DateField(verbose_name='Дата выполнения', auto_now_add=False, null=True, blank=True)


    def __str__(self):
        return f'{self.id}. {self.description}'
