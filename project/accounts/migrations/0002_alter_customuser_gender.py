# Generated by Django 4.2.4 on 2023-08-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="gender",
            field=models.IntegerField(choices=[(1, "male"), (2, "female")], default=1),
        ),
    ]
