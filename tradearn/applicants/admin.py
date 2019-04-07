from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):

    search_fields =(
        'representName',
        'patentApplicantNumber',
        'representNameFirm',
    )
    
    list_filter = (
        'representName',
        'add_date',
        'representNameFirm',
        'socialNumberFirmPresident'
    )

    list_display = (
        'representName',
        'representNameFirm',
        'patentApplicantNumber',
    )