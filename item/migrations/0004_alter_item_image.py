# Generated by Django 4.1.10 on 2023-07-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0003_alter_category_slug_item_item_item_id_88eba3_idx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="item_images/%Y/%m/%d"
            ),
        ),
    ]
