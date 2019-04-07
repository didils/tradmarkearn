from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

# Create your views here.

class GetAllQuestion(APIView):

    def get(self, request, format=None):

        all_question = models.Question.objects.all()

        serializer = serializers.QuestionSerializer(
            all_question, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)