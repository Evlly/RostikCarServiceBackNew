# Generated by Django 3.2.9 on 2022-01-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Клиент', 'Client'), ('Администратор', 'Administrator'), ('Механик', 'Mechanic'), ('Менеджер', 'Manager')], default='Клиент', max_length=13, verbose_name='Роль'),
        ),
    ]
