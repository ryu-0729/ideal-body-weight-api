from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import BodyDataSerializer, WeightCalculationSerializer


class BodyDataCreateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token_str = str(request.META["HTTP_AUTHORIZATION"]).replace("Bearer ", "", 1)
        access_token = AccessToken(token_str)

        user = get_object_or_404(CustomUser, id=access_token["user_id"])

        serializer = BodyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.bodydata_set.create(**serializer.validated_data)
        return Response(serializer.data, status.HTTP_201_CREATED)


class WeightCalculationAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = WeightCalculationSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)
