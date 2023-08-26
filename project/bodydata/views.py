from rest_framework import permissions, status, views
from rest_framework.response import Response

from .serializers import BodyDataSerializer, WeightCalculationSerializer


class BodyDataCreateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = BodyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.bodydata_set.create(**serializer.validated_data)
        return Response(serializer.data, status.HTTP_201_CREATED)


class WeightCalculationAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = WeightCalculationSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)
