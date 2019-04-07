from rest_framework import serializers
from . import models
from tradearn.users import models as user_models


class ApplicantUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class ApplicantSerializer(serializers.ModelSerializer):

    owner = ApplicantUserSerializer()

    class Meta:
        model = models.Applicant
        fields = (
            'address',
            'representName',
            'representNameEn',
            'patentApplicantNumber',
            'socialNumber',
            'socialNumberFirm',
            'socialNumberFirmReg',
            'representNameFirm',
            'socialNumberFirmPresident',
            'add_date',
            'owner'
        )


class ApplicantUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Applicant
        fields = (
            'address',
            'representName',
            'representNameEn',
            'patentApplicantNumber',
            'socialNumber',
            'socialNumberFirm',
            'socialNumberFirmReg',
            'representNameFirm',
            'socialNumberFirmPresident',
        )
