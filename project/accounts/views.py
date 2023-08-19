from rest_framework import generics

from .serializers import AccountSerializer


class AccountCreateAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer
