from django.contrib import admin

from .models import Servo


@admin.register(Servo)
class Servo(admin.ModelAdmin):
    pass
