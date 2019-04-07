from rest_framework import serializers
from . import models
from tradearn.users import models as user_models
from tradearn.casefiles import models as casefile_models


class OareportUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class OareportCasefileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = casefile_models.Casefile
        fields = (
            'file_name',
            'file_pdf'
        )


class OareportSerializer(serializers.ModelSerializer):

    owner = OareportUserSerializer()
    casefile = OareportCasefileSerializer()
    
    class Meta:
        model = models.OAreport
        fields = (
            'id',
            'casefile',
            'owner',
            'is_notified',
            'date_of_file',
            'price',
            'possibility',
            'examinerComment',
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
        model = models.OAreport
        fields = (
            'casefile',
            'owner',
            'clientGiveup',
        )