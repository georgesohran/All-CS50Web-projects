# Generated by Django 5.0.2 on 2024-03-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0018_post_edited"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="edited",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]