# Generated by Django 5.0.1 on 2024-01-20 15:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0002_bid_auction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auction",
            name="current_bid_id",
        ),
        migrations.AddField(
            model_name="auction",
            name="category",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name="auction",
            name="time",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="auction",
            name="description",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="auction",
            name="image",
            field=models.ImageField(blank=True, upload_to=""),
        ),
        migrations.CreateModel(
            name="Auction_Bid",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "auction_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auctions.auction",
                    ),
                ),
                (
                    "bid_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auctions.bid"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contents", models.CharField(max_length=1024)),
                (
                    "auction_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auctions.auction",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
