from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Casefile)
class CasefileAdmin(admin.ModelAdmin):

    search_fields =(
        'case',
        'owner',
        'date_of_file',
        'file_name',
    )
    
    list_filter = (
        'case',
        'owner',
        'date_of_file',
        'file_name',
    )

    list_display = (
        'case',
        'owner',
        'date_of_file',
        'file_name',
    )