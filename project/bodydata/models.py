from accounts.models import CustomUser
from django.db import models


class BodyData(models.Model):
    class Meta:
        db_table = "body_data"

    height = models.FloatField(verbose_name="身長")
    weight = models.FloatField(verbose_name="体重")
    created_at = models.DateField(verbose_name="登録日時", auto_now=True, unique=True)
    account = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
