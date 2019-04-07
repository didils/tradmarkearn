from django.shortcuts import render
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ApplicantCheck(APIView):

    def get(self, request, format=None):

        usernameforcheck = request.query_params.get('usernameforcheck', None)

        foundapplicant = models.Applicant.objects.filter(
                owner__username=usernameforcheck).order_by('add_date')[:10]

        serializer = serializers.ApplicantSerializer(
            foundapplicant, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UploadApplicants(APIView):

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.ApplicantUploadSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(owner=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
