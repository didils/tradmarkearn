from rest_framework import serializers
from . import models
from tradearn.users import models as user_models


class PointUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class PointSerializer(serializers.ModelSerializer):

    owner = PointUserSerializer()

    class Meta:
        model = models.Point_history
        fields = (
            'owner',
            'point_name',
            'add_date',
            'change_amount',
            'use_status',
        )


class PointUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Point_history
        fields = (
            'point_name',
            'change_amount',
            'use_status',
        )
