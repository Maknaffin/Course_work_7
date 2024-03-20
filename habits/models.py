from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=300, verbose_name='Действие')
    is_nice = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    period = models.PositiveIntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    action_time = models.PositiveIntegerField(verbose_name='Время выполнения привычки', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')
    good_habit = models.BooleanField(default=False, verbose_name='Полезная привычка')

    def __str__(self):
        return f'{self.pk}: {self.action} - {self.time}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
