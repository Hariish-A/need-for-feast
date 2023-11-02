# Generated by Django 4.2.6 on 2023-11-02 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_items_order_customer_deliverer_owner_restaurant_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addresses",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
