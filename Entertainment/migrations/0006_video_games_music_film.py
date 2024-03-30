# Generated by Django 4.2.3 on 2024-03-28 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Entertainment", "0005_subcategories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video_Games",
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
                ("question", models.TextField()),
                ("choices", models.TextField(blank=True, default=list)),
                ("correct_answer", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        default=2,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="Entertainment.categories",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Entertainment.subcategories",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Music",
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
                ("question", models.TextField()),
                ("choices", models.TextField(blank=True, default=list)),
                ("correct_answer", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        default=2,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="Entertainment.categories",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        default=3,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Entertainment.subcategories",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Film",
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
                ("question", models.TextField()),
                ("choices", models.TextField(blank=True, default=list)),
                ("correct_answer", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        default=2,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="Entertainment.categories",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        default=2,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Entertainment.subcategories",
                    ),
                ),
            ],
        ),
    ]
