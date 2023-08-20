from accounts.views import AccountCreateAPIView
from bodydata.views import BodyDataCreateAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("account/create/", AccountCreateAPIView.as_view(), name="account_create"),
    path("bodydata/create/", BodyDataCreateAPIView.as_view(), name="bodydata_create"),
]
