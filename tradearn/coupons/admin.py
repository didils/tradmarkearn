from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):

    search_fields =(
        'expire_date',
        'discount_amount',
        'discount_rate',
        'coupon_name',
        'coupon_type',
    )
    
    list_filter = (
        'expire_date',
        'discount_amount',
        'discount_rate',
        'coupon_name',
        'coupon_type',
    )

    list_display = (
        'id',
        'expire_date',
        'discount_amount',
        'discount_rate',
        'coupon_name',
        'coupon_type',
    )
