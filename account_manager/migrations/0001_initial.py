# Generated by Django 4.2 on 2023-05-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("article_manager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataLinker",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "article_list",
                    models.ManyToManyField(
                        related_name="article_list_str", to="article_manager.article"
                    ),
                ),
                (
                    "followed_user_list",
                    models.ManyToManyField(
                        related_name="followed_user_list_str",
                        to="account_manager.datalinker",
                    ),
                ),
            ],
        ),
    ]
