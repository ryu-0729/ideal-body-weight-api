from rest_framework import generics, permissions

from .models import CustomUser
from .serializers import AccountSerializer


class AccountCreateAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer


class AccountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all().prefetch_related("bodydata_set")
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
