from django.conf.urls import url
from . import views

app_name = "coupons"

urlpatterns = [
    url(
        regex=r'^check/$',
        view=views.CouponCheck.as_view(),
        name='coupon_check')
]