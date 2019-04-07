from django.db import models
from tradearn.users import models as user_models
from tradearn.cases import models as case_models
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose

class Casefile(models.Model):
    
    FILE_NAME = (
        ('위임 약정서','위임 약정서'),
        ('상표 등록 출원서','상표 등록 출원서'),
        ('의견 제출 통지서','의견 제출 통지서'),
        ('등록 결정서','등록 결정서'),
        ('거절 결정서','거절 결정서'),
        ('상표 등록증','상표 등록증'),
        ('기타 서류','기타 서류'),
    )
    
    # 주인이 사라졌을 때, 종속되어 있는 아이들을 어떻게 할것인가? 를 지정해 줘야 하는듯, on_delete=models.PROTECT를 넣어서 해결
    case = models.ForeignKey(case_models.Case, null=True, on_delete=models.PROTECT)
    owner = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    date_of_file = models.DateField(auto_now_add=True)
    file_pdf = models.FileField(null=True)
    isReportExist = models.BooleanField(default=False)
    expireDate = models.DateField(null=True, blank=True)
    # file_page1 = ProcessedImageField(processors=[
    #                                Transpose()
    #                            ],
    #                            format='JPEG',
    #                            options={'quality': 50})
    # file_page2 = ProcessedImageField(processors=[
    #                                Transpose()
    #                            ],
    #                            format='JPEG',
    #                            options={'quality': 50},
    #                            blank=True, null=True)
    # file_page3 = ProcessedImageField(processors=[
    #                                Transpose()
    #                            ],
    #                            format='JPEG',
    #                            options={'quality': 50},
    #                            blank=True, null=True)
    # file_page4 = ProcessedImageField(processors=[
    #                                Transpose()
    #                            ],
    #                            format='JPEG',
    #                            options={'quality': 50},
    #                            blank=True, null=True)
    # file_page5 = ProcessedImageField(processors=[
    #                                Transpose()
    #                            ],
    #                            format='JPEG',
    #                            options={'quality': 50},
    #                            blank=True, null=True)
    file_name = models.CharField(max_length=80, choices=FILE_NAME, blank=True, null=True)


    def __str__(self):
        return '상표명: {}({}) - {}'.format(self.case.trademark_title, self.owner.username, self.file_name)