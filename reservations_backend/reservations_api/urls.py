from django.urls import path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from rest_framework import routers, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

router = routers.SimpleRouter()
router.register(r"addresses", views.AddressViewSet)
router.register(r"customers", views.CustomerViewSet)
router.register(r"facilities", views.FacilityViewSet)
router.register(r"reservations", views.ReservationViewSet)

urlpatterns = [
    # schema endpoints
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # JWT Token authentication endpoints
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=[permissions.AllowAny]),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=[permissions.AllowAny]),
        name="token_refresh",
    ),
    # other API endpoints
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("test/", views.TestView.as_view()),
]

urlpatterns += router.urls
