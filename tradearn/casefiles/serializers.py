from rest_framework import serializers
from . import models
from tradearn.users import models as user_models
from tradearn.cases import models as case_models


class CasefileUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class CasefileCaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = case_models.Case
        fields = (
            'trademark_title',
            'application_number',
            'identification_number'
        )

class CasefileSerializer(serializers.ModelSerializer):

    owner = CasefileUserSerializer()
    case = CasefileCaseSerializer()
    
    class Meta:
        model = models.Casefile
        fields = (
            'id',
            'case',
            'owner',
            'date_of_file',
            # 'file_page1',
            # 'file_page2',
            # 'file_page3',
            # 'file_page4',
            # 'file_page5',
            'file_name',
            'file_pdf',
            'isReportExist',
            'expireDate'
        )