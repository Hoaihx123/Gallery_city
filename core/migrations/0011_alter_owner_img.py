# Generated by Django 4.2.5 on 2023-09-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_artist_img_exhibit_img_gallery_img_owner_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="img",
            field=models.ImageField(blank=True, default="img.jpg", upload_to="owners"),
        ),
    ]