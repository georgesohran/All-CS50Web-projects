# Generated by Django 5.0.1 on 2024-01-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_auction_winner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auction",
            name="description",
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
