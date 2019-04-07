from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Point_history)
class Point_HistoryAdmin(admin.ModelAdmin):

    search_fields =(
        'owner',
        'add_date',
        'use_status',
    )
    
    list_filter = (
        'owner',
        'add_date',
        'use_status',
    )

    list_display = (
        'owner',
        'add_date',
        'change_amount',
        'use_status',
    )