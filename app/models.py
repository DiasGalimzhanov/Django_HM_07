from xml.dom import ValidationErr
from django.db import models
from django.core import validators
import datetime
from django.forms import ValidationError

class Todo(models.Model):
    class Status(models.TextChoices):
        CREATED = 'c', 'created'
        IN_PROGRESS = 'i', 'in progress'
        DONE = 'd', 'completed'

    title = models.CharField(max_length=255, validators=[validators.MinLengthValidator(5)],verbose_name='Заголовок')
    body = models.TextField(validators=[validators.MaxLengthValidator(255), validators.MinLengthValidator(20)],verbose_name='Описание')
    deadline = models.DateField(verbose_name='Дудлайн')
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.CREATED, verbose_name='Статус')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title



