# Generated by Django 5.0.4 on 2024-09-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("slmsapp", "0006_staff_leave"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[(1, "admin"), (2, "staff")], default=1, max_length=50
            ),
        ),
    ]
