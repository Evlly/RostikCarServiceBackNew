from django.contrib import admin
from apps.module.models import Module, Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass
