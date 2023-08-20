from rest_framework import serializers

from .models import BodyData


class BodyDataSerializer(serializers.ModelSerializer):
    """身体データ用のシリアライザ"""

    class Meta:
        model = BodyData
        fields = ["height", "weight", "created_at"]
