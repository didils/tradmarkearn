from django.db import models
from tradearn.users import models as user_models

class Applicant(models.Model):

# Create your models here.

    address = models.CharField(max_length=140, blank=True, null=True)
    representName = models.CharField(max_length=140, blank=True, null=True)
    representNameEn = models.CharField(max_length=140, blank=True, null=True)
    patentApplicantNumber = models.CharField(max_length=140, blank=True, null=True)
    socialNumber = models.CharField(max_length=140, blank=True, null=True)
    socialNumberFirm = models.CharField(max_length=140, blank=True, null=True)
    socialNumberFirmReg = models.CharField(max_length=140, blank=True, null=True)
    representNameFirm = models.CharField(max_length=140, blank=True, null=True)
    socialNumberFirmPresident = models.CharField(max_length=140, blank=True, null=True)
    add_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)