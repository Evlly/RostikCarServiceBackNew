from django.contrib.auth import get_user_model
from django.db import models
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel


User = get_user_model()


class Module(LifecycleModelMixin, UUIDModel):
    name = models.CharField('Название', max_length=32, unique=True)


class Config(LifecycleModelMixin, UUIDModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enable = models.BooleanField('Статус')
