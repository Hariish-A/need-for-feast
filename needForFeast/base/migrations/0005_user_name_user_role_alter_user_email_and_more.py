# Generated by Django 4.2.6 on 2023-10-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_remove_addresses_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("OWNER", "Owner"),
                    ("CUSTOMER", "Customer"),
                    ("DELIVERER", "Deliverer"),
                ],
                default="ADMIN",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]