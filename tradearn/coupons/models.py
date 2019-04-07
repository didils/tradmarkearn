from django.db import models
from tradearn.users import models as user_models

class Coupon(models.Model):

    STATUS_CHOICES = (
        ('비율할인','비율할인'),
        ('원플러스원','원플러스원'),
        ('금액할인','금액할인'),
    )

# Create your models here.
    
    expire_date = models.DateField(blank=True, null=True)
    discount_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    discount_amount = models.PositiveSmallIntegerField(blank=True, null=True)
    coupon_name = models.CharField(max_length=80, blank=True, null=True)
    coupon_type = models.CharField(max_length=80, choices=STATUS_CHOICES, blank=True, null=True)
    add_date = models.DateField(auto_now_add=True)