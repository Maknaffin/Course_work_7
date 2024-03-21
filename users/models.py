from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    chat_id = models.TextField(verbose_name='id чата в телеграмме', **NULLABLE)
    telegram_user_name = models.CharField(max_length=200, verbose_name='Имя в телеграмме', unique=True, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
