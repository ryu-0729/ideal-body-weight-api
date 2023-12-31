from bodydata.serializers import BodyDataSerializer
from rest_framework import serializers

from .models import CustomUser


class AccountSerializer(serializers.ModelSerializer):
    """アカウント用のシリアライザ"""

    bodydata_set = BodyDataSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "gender",
            "password",
            "bodydata_set",
        ]


class AccountRequestSerializer(serializers.ModelSerializer):
    """アカウントリクエスト用のシリアライザ"""

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "gender",
            "password",
        ]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class AccountResponseSerializer(serializers.ModelSerializer):
    """アカウントレスポンス用のシリアライザ"""

    bodydata_set = BodyDataSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "gender",
            "bodydata_set",
        ]
