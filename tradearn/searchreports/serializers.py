from rest_framework import serializers
from . import models
from tradearn.users import models as user_models
from tradearn.cases import models as case_models


class searchreportUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class searchreportCaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = case_models.Case
        fields = (
            'id',
            'trademark_title',
            'application_number',
            'identification_number'
        )


class searchreportSerializer(serializers.ModelSerializer):

    owner = searchreportUserSerializer()
    case = searchreportCaseSerializer()
    
    class Meta:
        model = models.searchreport
        fields = (
            'id',
            'case',
            'owner',
            'is_notified',
            'date_of_file',
            'date_of_file',
            'possibility',
            
            'attorneyComment',
            'image1',
            'date_of_image1',
            'applicant1',
            'application_number1',
            'image2',
            'date_of_image2',
            'applicant2',
            'application_number2',
            'image3',
            'date_of_image3',
            'applicant3',
            'application_number3',
            'image4',
            'date_of_image4',
            'applicant4',
            'application_number4',
            'image5',
            'date_of_image5',
            'applicant5',
            'application_number5',
        )

class ApplicantUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.searchreport
        fields = (
            'case',
            'owner',
            'clientGiveup',
        )