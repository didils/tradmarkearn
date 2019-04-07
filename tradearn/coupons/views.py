from django.shortcuts import render
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CouponCheck(APIView):

    def get(self, request, format=None):

        foundcoupon = models.Coupon.objects.all()

        serializer = serializers.CouponSerializer(
            foundcoupon, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)
