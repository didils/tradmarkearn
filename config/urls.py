from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path("users/", include("tradearn.users.urls", namespace="users")),
    path(
        "cases/",
        include("tradearn.cases.urls", namespace="cases"),
    ),
    path(
        "oareports/",
        include("tradearn.OAreports.urls", namespace="reports"),
    ),
    path(
        "searchreports/",
        include("tradearn.searchreports.urls", namespace="searchreports"),
    ),
    path(
        "applicants/",
        include("tradearn.applicants.urls", namespace="applicants"),
    ),
    path(
        "questions/",
        include("tradearn.questions.urls", namespace="questions"),
    ),
    path(
        "casefiles/",
        include("tradearn.casefiles.urls", namespace="casefiles"),
    ),
    path(
        "coupons/",
        include("tradearn.coupons.urls", namespace="coupons"),
    ),
    # path(
    #     "relations/",
    #     include("tradearn.relations.urls", namespace="relations"),
    # ),
    path(
        "products/",
        include("tradearn.products.urls", namespace="products"),
    ),
    path(
        "pointhistories/",
        include("tradearn.point_histories.urls", namespace="point_histories"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns