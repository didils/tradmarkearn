from django.conf.urls import url
from . import views

app_name = "searchreports"

urlpatterns = [
    url(
        regex=r'^check/$',
        view=views.searchreportCheck.as_view(),
        name='searchreport_check'),
    url(
        regex=r'^notifycheck/$',
        view=views.searchreportNotifyCheck.as_view(),
        name='searchreport_notify_check'),
]