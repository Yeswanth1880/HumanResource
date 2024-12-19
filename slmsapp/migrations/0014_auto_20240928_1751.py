# Generated by Django 3.1.5 on 2024-09-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0013_staff_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'staff'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
