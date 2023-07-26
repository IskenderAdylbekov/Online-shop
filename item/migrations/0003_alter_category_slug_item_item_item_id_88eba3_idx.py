# Generated by Django 4.1.10 on 2023-07-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0002_alter_category_options_category_slug_item_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AddIndex(
            model_name="item",
            index=models.Index(fields=["id", "slug"], name="item_item_id_88eba3_idx"),
        ),
    ]
