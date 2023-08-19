from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = "custom_user"

    objects = UserManager()

    GENDER_TYPE = (
        (1, "男性"),
        (2, "女性"),
    )

    gender = models.IntegerField(verbose_name="性別", choices=GENDER_TYPE, default=1)
