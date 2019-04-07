from django.shortcuts import render
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class searchreportCheck(APIView):

    def get(self, request, format=None):

        idforcheck = request.query_params.get('idforcheck', None)

        foundreport = models.searchreport.objects.filter(
                case__id=idforcheck)

        # foundreport = models.searchreport.objects.all()

        serializer = serializers.searchreportSerializer(
            foundreport, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class searchreportNotifyCheck(APIView):

    def get(self, request, format=None):

        usernameforcheck = request.query_params.get('usernameforcheck', None)

        foundreport = models.searchreport.objects.filter(
                owner__username=usernameforcheck).filter(is_notified=False)

        serializer = serializers.searchreportSerializer(
            foundreport, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):

        idforcheck = request.query_params.get('idforcheck', None)

        foundreport = models.searchreport.objects.get(
                id=idforcheck)

                

        if foundreport is not None:

            foundreport.is_notified = True

            foundreport.save()

            return Response(status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
