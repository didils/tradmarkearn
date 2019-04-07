from rest_framework import serializers
from . import models

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = (
            'id',
            'add_date',
            'question_title',
            'category',
            'question_detail'
        )