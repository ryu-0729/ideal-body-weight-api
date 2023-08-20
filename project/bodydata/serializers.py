from decimal import ROUND_HALF_UP, Decimal

from rest_framework import serializers

from .models import BodyData


class BodyDataSerializer(serializers.ModelSerializer):
    """身体データ用のシリアライザ"""

    class Meta:
        model = BodyData
        fields = ["height", "weight", "created_at"]


class WeightCalculationSerializer(serializers.Serializer):
    """理想の体重計算用のシリアライザ"""

    height = serializers.FloatField()
    weight = serializers.FloatField()
    bmi = serializers.SerializerMethodField()
    appropriate_body_weight = serializers.SerializerMethodField()
    beauty_weight = serializers.SerializerMethodField()
    cinderella_weight = serializers.SerializerMethodField()

    def height_squared(self, height: float) -> float:
        """身長をcm→mに変換し2乗する"""
        return (height / 100) ** 2

    def round_up_and_down(self, target):
        """四捨五入メソッド"""
        exp = Decimal("0.1")
        return str(Decimal(target).quantize(exp, ROUND_HALF_UP))

    def get_bmi(self, obj):
        return self.round_up_and_down(
            obj["weight"] / self.height_squared(obj["height"])
        )

    def get_appropriate_body_weight(self, obj):
        return self.round_up_and_down(self.height_squared(obj["height"]) * 22)

    def get_beauty_weight(self, obj):
        return self.round_up_and_down(self.height_squared(obj["height"]) * 20)

    def get_cinderella_weight(self, obj):
        return self.round_up_and_down(self.height_squared(obj["height"]) * 18)
