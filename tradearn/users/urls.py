from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
    url(
        regex=r'^(?P<username>\w+)/password/$',
        view=views.ChangePassword.as_view(),
        name='change'
    ),
    url(
        regex=r'^self/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
    url(
        regex=r'^check/$',
        view=views.DuplicateCheck.as_view(),
        name='username_check')
        ,
    url(
        regex=r'^checkemail/$',
        view=views.DuplicateEmailCheck.as_view(),
        name='email_check')
        ,
    url(
        regex=r'^checkid/$',
        view=views.DuplicateIdCheck.as_view(),
        name='id_check'),
    url(
        regex=r'^login/facebook/$',
        view=views.FacebookLogin.as_view(),
        name='fb_login'),
    url(
        regex=r'^getprofile/$',
        view=views.UserProfile.as_view(),
        name='Get_profile'),
    url(
        regex=r'^updatepoint/$',
        view=views.UpdateUserPoint.as_view(),
        name='update_point')
]