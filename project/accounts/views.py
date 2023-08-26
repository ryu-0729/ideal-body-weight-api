from drf_rw_serializers import generics
from rest_framework import permissions, status, views
from rest_framework.response import Response

from .models import CustomUser
from .serializers import (
    AccountRequestSerializer,
    AccountResponseSerializer,
    AccountSerializer,
)


class AccountCreateAPIView(generics.CreateAPIView):
    # TODO: serializer_classを追加しないとBrowsable APIが動かない
    # https://github.com/vintasoftware/drf-rw-serializers/issues/44
    serializer_class = AccountSerializer
    read_serializer_class = AccountRequestSerializer
    write_serializer_class = AccountResponseSerializer


class AccountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all().prefetch_related("bodydata_set")
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountMypageAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = AccountResponseSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)
