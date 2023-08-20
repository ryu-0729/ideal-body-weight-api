from accounts.models import CustomUser
from django.db import models


class BodyData(models.Model):
    class Meta:
        db_table = "body_data"

    height = models.FloatField(verbose_name="身長")
    weight = models.FloatField(verbose_name="体重")
    created_at = models.DateField(verbose_name="登録日時", unique=True)
    account = models.ForeignKey(
        CustomUser,
        verbose_name="アカウント",
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return str(self.pk)
