from django.contrib import admin
from .models import Checks

@admin.register(Checks)
class AdminChecks(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'check_number', 'money')
    search_fields = ('title',)
    list_filter = ('title',)