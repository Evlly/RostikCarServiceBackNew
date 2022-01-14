from tabnanny import verbose
from tokenize import Name
from unicodedata import name
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel
from django.db import models


class TypeService(LifecycleModelMixin, UUIDModel):
    name = models.CharField('Название', max_length=32, unique=True)


class Service(LifecycleModelMixin, UUIDModel):
    name = models.CharField('Название', max_length=128)
    type = models.ForeignKey(TypeService, models.SET_NULL, null=True)
    description = models.TextField('Описание')
    # TODO: popularity
