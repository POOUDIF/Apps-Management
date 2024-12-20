from django.contrib import admin

from .models import BBIToken


@admin.register(BBIToken)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'username', 'created', 'expires',)
    fields = ('username',)
    ordering = ('-expires',)
