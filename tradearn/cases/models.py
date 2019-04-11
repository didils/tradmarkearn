from django.contrib.postgres.fields import JSONField
from django.db import models
from tradearn.users import models as user_models
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose

class Case(models.Model):

    STATUS_CHOICES = (
        ('결제 대기 중','결제 대기 중'),
        ('출원 준비 중','출원 준비 중'),
        ('심사 중','심사 중'),
        ('출원공고','출원공고'),
        ('거절 대응 중','거절 대응 중'),
        ('등록 결정','등록 결정'),
        ('등록 완료','등록 완료'),
        ('갱신 대상','갱신 대상'),
    )

    trademark_title = models.CharField(max_length=80, null=True, blank=True)
    file = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50}, null=True, blank=True)
    
    
    # 주인이 사라졌을 때, 종속되어 있는 아이들을 어떻게 할것인가? 를 지정해 줘야 하는듯, on_delete=models.PROTECT를 넣어서 해결
    owner = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    
    # examiner 관한 사항 추가 examiner = models.ForeignKey(examiner_models.Examiner, null=True, on_delete=models.PROTECT) import도 역시 해야 함.
    
    # payment  관한 사항 추가 payment = models.ForeignKey(payment_models.Payment, null=True, on_delete=models.PROTECT) import도 역시 해야 함.
    # 여러 사건이 하나의 결제로 이루어질 경우, 각 사건이 하나의 결제를 참조(포인팅)할 수 있다.

    request_date = models.DateField(auto_now_add=True)
    payment_date = models.DateField(null=True, blank=True)
    filed_date = models.DateField(null=True, blank=True)
    application_number = models.CharField(max_length=80, null=True, blank=True)
    identification_number = models.CharField(max_length=80, null=True, blank=True)
    publication_number = models.CharField(max_length=80, blank=True, null=True)
    publication_date = models.DateField(null=True, blank=True)
    registration_number = models.CharField(max_length=80, blank=True, null=True)
    registration_date = models.DateField(null=True, blank=True)
    products = models.TextField(blank=True, null=True)
    designatedArray = models.TextField(blank=True, null=True)
    applicantArray = models.TextField(blank=True, null=True)
    paymentArray = models.TextField(blank=True, null=True)
    descriptions = models.TextField(blank=True, null=True)
    progress_status = models.CharField(max_length=80, choices=STATUS_CHOICES, blank=True, null=True)

    expected_date = models.DateField(null=True, blank=True)
    examiner_name = models.CharField(max_length=80, blank=True, null=True)
    examiner_phone = models.CharField(max_length=80, blank=True, null=True)
    examiner_team = models.CharField(max_length=80, blank=True, null=True)
    waiting_order = models.PositiveSmallIntegerField(blank=True, null=True)
    waiting_total = models.PositiveSmallIntegerField(blank=True, null=True)

    
    def __str__(self):
        return '상표명: {} - 출원인: {}'.format(self.trademark_title, self.owner.username)