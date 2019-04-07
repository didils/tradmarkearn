from django.conf.urls import url
from . import views

app_name = "applicants"

urlpatterns = [
    url(
        regex=r'^check/$',
        view=views.ApplicantCheck.as_view(),
        name='applicant_check'),
    url(
        regex=r'^uploads/$',
        view=views.UploadApplicants.as_view(),
        name='upload_applicants'
    )
]