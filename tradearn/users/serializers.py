from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from . import models
# from tradearn.images import serializers as images_serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            
            'username',
            'name',
            'email',
            'point',
            'phone',
            'address',
            'point',
        )


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'email',
            'point',
            'phone',
            'address',
            'point',
            'coupon_history',
            'cumulative_pay_amount'
        )


class SignUpSerializer(RegisterSerializer):

    name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'social_id': self.validated_data.get('social_id', ''),
            'phone': self.validated_data.get('phone', ''),
            'fcm_pushtoken': self.validated_data.get('fcm_pushtoken', '')
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user