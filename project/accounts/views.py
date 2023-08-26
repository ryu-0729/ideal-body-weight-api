from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from .models import CustomUser
from .serializers import AccountResponseSerializer, AccountSerializer


class AccountCreateAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer


class AccountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all().prefetch_related("bodydata_set")
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountMypageAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = AccountResponseSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)
