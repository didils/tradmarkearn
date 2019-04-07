from django.conf.urls import url
from . import views

app_name = "OAreports"

urlpatterns = [
    url(
        regex=r'^check/$',
        view=views.OAreportCheck.as_view(),
        name='oareport_check'),
    url(
        regex=r'^notifycheck/$',
        view=views.OAreportNotifyCheck.as_view(),
        name='oareport_notify_check'),
]