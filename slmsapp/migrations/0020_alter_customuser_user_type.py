# Generated by Django 5.1.1 on 2024-09-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slmsapp", "0019_rename_department_staff_dept"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[(2, "staff"), (1, "admin")], default=1, max_length=50
            ),
        ),
    ]
