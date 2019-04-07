from django.conf.urls import url
from . import views

app_name = "cases"

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllCases.as_view(),
        name='all_cases'
    ),
    url(
        regex=r'^upload/$',
        view=views.UploadCases.as_view(),
        name='upload_case'
    ),
    url(
        regex=r'^uploads/$',
        view=views.UploadsCases.as_view(),
        name='upload_cases'
    )
]