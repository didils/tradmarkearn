from django.conf.urls import url
from . import views

app_name = "casefiles"

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllCasefiles.as_view(),
        name='all_case_files'
    ),
    url(
        regex=r'^upload/$',
        view=views.UploadCasefiles.as_view(),
        name='upload_case_files'
    )
]