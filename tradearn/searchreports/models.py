from django.db import models
from tradearn.users import models as user_models

from tradearn.cases import models as case_models
from imagekit.models import ProcessedImageField
from imagekit.processors import Transpose

# Create your models here.

class searchreport(models.Model):
    
    
    case = models.ForeignKey(case_models.Case, null=True, on_delete=models.PROTECT)
    owner = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    date_of_file = models.DateField(auto_now_add=True)
    
    possibility	= models.PositiveSmallIntegerField(blank=True, null=True)
    
    attorneyComment = models.TextField(blank=True, null=True)
    clientGiveup = models.BooleanField(default=False)
    is_notified = models.BooleanField(default=False)
    image1 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    date_of_image1 = models.DateField(blank=True, null=True)
    application_number1 = models.CharField(max_length=80, blank=True, null=True)
    applicant1 = models.CharField(max_length=80, blank=True, null=True)
    image2 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    date_of_image2 = models.DateField(blank=True, null=True)
    application_number2 = models.CharField(max_length=80, blank=True, null=True)
    applicant2 = models.CharField(max_length=80, blank=True, null=True)
    image3 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    date_of_image3 = models.DateField(blank=True, null=True)
    application_number3 = models.CharField(max_length=80, blank=True, null=True)
    applicant3 = models.CharField(max_length=80, blank=True, null=True)
    image4 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    date_of_image4 = models.DateField(blank=True, null=True)
    application_number4 = models.CharField(max_length=80, blank=True, null=True)
    applicant4 = models.CharField(max_length=80, blank=True, null=True)
    image5 = ProcessedImageField(processors=[
                                   Transpose()
                               ],
                               format='JPEG',
                               options={'quality': 50},
                               blank=True, null=True)
    date_of_image5 = models.DateField(blank=True, null=True)
    application_number5 = models.CharField(max_length=80, blank=True, null=True)
    applicant5 = models.CharField(max_length=80, blank=True, null=True)