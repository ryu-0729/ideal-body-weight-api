from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = "custom_user"

    GENDER_TYPE = (
        (1, "男性"),
        (2, "女性"),
    )

    gender = models.IntegerField(verbose_name="性別", choices=GENDER_TYPE, default=1)
