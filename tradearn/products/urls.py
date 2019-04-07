from django.conf.urls import url
from . import views

app_name = "products"

urlpatterns = [
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    ),
    url(
        regex=r'^uploadproducts/$',
        view=views.UploadProducts.as_view(),
        name='upload_products'
    )    
]