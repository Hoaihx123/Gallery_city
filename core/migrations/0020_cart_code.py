# Generated by Django 4.2.5 on 2023-10-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='code',
            field=models.ImageField(blank=True, upload_to='QR-code'),
        ),
    ]