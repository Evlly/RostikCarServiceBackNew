from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel
from django.db import models
from apps.user.models import User
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_CREATE
from rest_framework.exceptions import ValidationError


class Detail(LifecycleModelMixin, UUIDModel):
    name = models.CharField('Название', max_length=32, unique=False )
    price = models.DecimalField('Стоимость', max_digits=6, decimal_places=2, default=0)
    car = models.CharField('Автомобиль', max_length=32, unique=False)
    count = models.PositiveSmallIntegerField('Максимум активаций', default=0)

class TypeService(LifecycleModelMixin, UUIDModel):
    name = models.CharField('Название', max_length=32, unique=True)


class OrderStatus(LifecycleModelMixin, UUIDModel):
    name = models.CharField('Название', max_length=32, unique=True)


class Service(LifecycleModelMixin, UUIDModel):
    price = models.DecimalField('Стоимость', max_digits=6, decimal_places=2, default=0)
    name = models.CharField('Название', max_length=128)
    type = models.ForeignKey(TypeService, models.SET_NULL, null=True)
    description = models.TextField('Описание')


class Order(LifecycleModelMixin, UUIDModel):
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='staff_orders')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_orders')
    services = models.ManyToManyField(Service, verbose_name='Услуги')
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    @hook(BEFORE_CREATE)
    def by(self):
        price = sum([s.price for s in self.services.all()])
        if self.client.balance < price:
            raise ValidationError('Недостаточно средств')
        self.client.balance -= price
        self.client.save()
