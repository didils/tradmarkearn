from rest_framework import serializers
from . import models
from tradearn.users import models as user_models


class CaseUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'name'
        )

class CaseSerializer(serializers.ModelSerializer):

    owner = CaseUserSerializer()

    # 여기다가 username = 유저씨리얼라이져 추가해야 하는데, 왜 강좌가 안나오는거지
    # 추가했다!
    # 장고 버전업이 되면서, 특정 필드만 부르는 것이 금지되었음. 따라서, field에 '__all__'을 꼭 넣어야 함 -> 모든 필드 불러내는 듯

    class Meta:
        model = models.Case
        fields = (
            'id',
            'trademark_title',
            'file',
            'owner',
            'request_date',
            'payment_date',
            'filed_date',
            'application_number',
            'publication_number',
            'publication_date',
            'registration_number',
            'registration_date',
            'products',
            'progress_status',
            'designatedArray',
            'applicantArray',
            'paymentArray',
            'descriptions',
            'identification_number',
            'expected_date',
            'examiner_name',
            'examiner_phone',
            'examiner_team',
            'waiting_order',
            'waiting_total',
        )

class CaseUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Case
        fields = (
            'trademark_title',
            'file',
            'products',
            'designatedArray',
            'applicantArray',
            'descriptions',
            'progress_status',
            'identification_number'
        )

class CasesUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Case
        fields = (
            'trademark_title',
            'products',
            'designatedArray',
            'applicantArray',
            'descriptions',
            'progress_status',
            'identification_number'
        )