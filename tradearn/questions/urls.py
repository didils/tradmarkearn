from django.conf.urls import url
from . import views

app_name = "questions"

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.GetAllQuestion.as_view(),
        name='question_getall'),
]

 

