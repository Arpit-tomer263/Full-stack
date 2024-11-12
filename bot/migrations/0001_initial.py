# Generated by Django 5.0.1 on 2024-09-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=12)),
                ("email", models.CharField(max_length=25)),
                ("description", models.TextField()),
            ],
        ),
    ]