from django.shortcuts import render
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class OAreportCheck(APIView):

    def get(self, request, format=None):

        idforcheck = request.query_params.get('idforcheck', None)

        foundreport = models.OAreport.objects.filter(
                casefile__id=idforcheck)

        serializer = serializers.OareportSerializer(
            foundreport, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class OAreportNotifyCheck(APIView):

    def get(self, request, format=None):

        usernameforcheck = request.query_params.get('usernameforcheck', None)

        foundreport = models.OAreport.objects.filter(
                owner__username=usernameforcheck).filter(is_notified=False)

        serializer = serializers.OareportSerializer(
            foundreport, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):

        idforcheck = request.query_params.get('idforcheck', None)

        foundreport = models.OAreport.objects.get(
                id=idforcheck)

                

        if foundreport is not None:

            foundreport.is_notified = True

            foundreport.save()

            return Response(status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
