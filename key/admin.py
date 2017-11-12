from django.contrib import admin

from .models import Key


@admin.register(Key)
class Key(admin.ModelAdmin):
    pass
