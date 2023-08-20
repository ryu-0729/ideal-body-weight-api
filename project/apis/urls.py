from accounts.views import AccountCreateAPIView, AccountRetrieveAPIView
from bodydata.views import BodyDataCreateAPIView, WeightCalculationAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("account/create/", AccountCreateAPIView.as_view(), name="account_create"),
    path("account/<pk>/", AccountRetrieveAPIView.as_view(), name="account_retrieve"),
    path("bodydata/create/", BodyDataCreateAPIView.as_view(), name="bodydata_create"),
    path(
        "bodydata/weight-calculation/",
        WeightCalculationAPIView.as_view(),
        name="weight_calculation",
    ),
]
