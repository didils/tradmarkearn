from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.OAreport)
class OAreportAdmin(admin.ModelAdmin):

    search_fields =(
        'casefile',
        'owner',
    )
    
    list_filter = (
        'casefile',
        'owner',
    )

    list_display = (
        'casefile',
        'owner',
    )