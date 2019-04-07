from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ListAllCasefiles(APIView):

    def get(self, request, format=None):
        
        print(request.user)

        user = request.user
        identification_number = request.query_params.get('identification_number', None)
        
        all_casefiles = models.Casefile.objects.filter(owner__username=user).filter(case__identification_number=identification_number)

        serializer = serializers.CasefileSerializer(all_casefiles, many=True, context={'request': request})

        return Response(data=serializer.data)

class UploadCasefiles(APIView):

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.CasefileUploadSerializer(data=request.data)


        if serializer.is_valid():

            serializer.save(owner=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)