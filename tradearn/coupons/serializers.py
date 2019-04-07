from rest_framework import serializers
from . import models
from tradearn.users import models as user_models


# class CouponUserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = user_models.User
#         fields = (
#             'username',
#             'name'
#         )

class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Coupon
        fields = (
            'id',
            'expire_date',
            'discount_amount',
            'discount_rate',
            'coupon_name',
            'coupon_type',
            'add_date',
        )