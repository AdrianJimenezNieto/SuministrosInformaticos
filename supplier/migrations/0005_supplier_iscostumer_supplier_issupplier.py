# Generated by Django 4.1.7 on 2023-03-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_remove_supplier_accesslevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='isCostumer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supplier',
            name='isSupplier',
            field=models.BooleanField(default=True),
        ),
    ]
