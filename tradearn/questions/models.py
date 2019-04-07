from django.db import models

class Question(models.Model):

    STATUS_CHOICES = (
        ('어플 사용 관련','어플 사용 관련'),
        ('변리사/특허법인 관련','변리사/특허법인 관련'),
        ('특허/디자인 업무 관련','특허/디자인 업무 관련'),
        ('해외 출원 관련','해외 출원 관련'),
        ('상표 출원 전반','상표 출원 전반'),
        ('비용 관련','비용 관련'),
        ('기타','기타'),
    )
# Create your models here.

    question_title = models.CharField(max_length=140, blank=True, null=True)
    category = models.CharField(max_length=80, choices=STATUS_CHOICES, blank=True, null=True)
    add_date = models.DateField(auto_now_add=True)
    question_detail = models.TextField(blank=True, null=True)
    