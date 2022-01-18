from django.contrib.auth.models import AbstractUser
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel, enum_max_length
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_lifecycle import LifecycleModelMixin


class UserRoles(models.TextChoices):
    CLIENT = 'Клиент'
    ADMINISTRATOR = 'Администратор'
    MECHANIC = 'Механик'


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    role = models.CharField('Роль', max_length=enum_max_length(UserRoles), choices=UserRoles.choices, default=UserRoles.CLIENT)
    middle_name = models.CharField('Отчество', max_length=32, default='', blank=True, null=True)
    car = models.CharField('Машина', max_length=32, default='', blank=True, null=True)
    phone = PhoneNumberField('Номер телефона', unique=True, help_text='Пример, +79510549236')
    balance = models.DecimalField('Баланс', max_digits=6, decimal_places=2, default=0)
    email = models.EmailField('Адрес электронной почты', default='')

    REQUIRED_FIELDS = ['email', 'phone']
