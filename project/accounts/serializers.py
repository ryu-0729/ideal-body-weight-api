from rest_framework import serializers

from .models import CustomUser


class AccountSerializer(serializers.ModelSerializer):
    """アカウント用のシリアライザ"""

    class Meta:
        model = CustomUser
        # TODO: email, passwordはレスポンスから外す
        fields = ["username", "first_name", "last_name", "email", "gender", "password"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
