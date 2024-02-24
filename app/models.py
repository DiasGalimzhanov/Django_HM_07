from xml.dom import ValidationErr
from django.db import models
from django.core import validators
from django.core.validators import BaseValidator
import datetime
from django.forms import ValidationError

class CustomValidator(BaseValidator):
    def __init__(self, limit_value):
        self.limit_value = limit_value
        message = f"Значение должно быть больше {limit_value}."
        super().__init__(limit_value, message)

    def __call__(self, value):
        if value <= self.limit_value:
            raise ValidationError(self.message)

class Todo(models.Model):
    class Status(models.TextChoices):
        CREATED = 'c', 'created'
        IN_PROGRESS = 'i', 'in progress'
        DONE = 'd', 'completed'

    title = models.CharField(max_length=255, validators=[validators.MinLengthValidator(5)],verbose_name='Заголовок')
    body = models.TextField(validators=[validators.MaxLengthValidator(255), validators.MinLengthValidator(20)],verbose_name='Описание')
    deadline = models.DateField(
        verbose_name='Дeдлайн',
        validators=[CustomValidator(datetime.date.today())]  
    )
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.CREATED, verbose_name='Статус')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title



