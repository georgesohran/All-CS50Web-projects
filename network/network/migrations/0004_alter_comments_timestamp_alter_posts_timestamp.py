# Generated by Django 5.0.2 on 2024-03-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0003_comments_timestamp_alter_comments_commented_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="posts",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]