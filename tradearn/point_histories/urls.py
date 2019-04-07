from django.conf.urls import url
from . import views

app_name = "point_histories"

urlpatterns = [
    url(
        regex=r'^check/$',
        view=views.Point_HistoryCheck.as_view(),
        name='point_history_check'),
    url(
        regex=r'^uploads/$',
        view=views.UploadPoint_Histories.as_view(),
        name='upload_point_histories'
    )
]