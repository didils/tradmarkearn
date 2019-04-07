from django.shortcuts import render
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Point_HistoryCheck(APIView):

    def get(self, request, format=None):

        usernameforcheck = request.query_params.get('usernameforcheck', None)

        found_point_history = models.Point_history.objects.filter(
                owner__username=usernameforcheck)

        serializer = serializers.PointSerializer(
            found_point_history, many=True, context={'request': request})
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UploadPoint_Histories(APIView):

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.PointUploadSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(owner=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
