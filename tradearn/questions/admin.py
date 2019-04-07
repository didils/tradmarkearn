from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):

    search_fields =(
        'question_title',
        'category',
        'add_date',
    )
    
    list_filter = (
        'category',
        'add_date',
        
    )

    list_display = (
        'question_title',
        'category',
        
    )