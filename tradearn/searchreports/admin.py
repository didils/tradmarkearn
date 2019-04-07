from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.searchreport)
class searchreportAdmin(admin.ModelAdmin):

    search_fields =(
        'case',
        'owner',
    )
    
    list_filter = (
        'case',
        'owner',
    )

    list_display = (
        'case',
        'owner',
    )