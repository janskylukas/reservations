from django.http import HttpResponse
from django.conf import settings
from rest_framework import viewsets, permissions, generics
# from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User

from reservations_core.models import (
    Address,
    Customer,
    Facility,
    Reservation,
)
from .serializers import (
    AddressSerializer,
    CustomerSerializer,
    FacilitySerializer,
    ReservationSerializer,
    UserSerializer,
)


# class CookieTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         data = response.data
#         refresh = response.data.get("refresh")
#         access = response.data.get("access")

#         response.set_cookie(
#             "refresh_token",
#             refresh,
#             httponly=True,
#             secure=settings.DEBUG is False,
#             samesite="Lax",
#         )

#         respon

#         return response


class TestView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.META["HTTP_ORIGIN"])
        return HttpResponse(content="XDDDDDDDD", status=200)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
