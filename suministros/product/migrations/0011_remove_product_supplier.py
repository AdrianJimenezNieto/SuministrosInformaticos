# Generated by Django 4.1.7 on 2023-04-12 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
    ]