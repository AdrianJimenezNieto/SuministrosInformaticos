# Generated by Django 4.1.7 on 2023-04-12 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_supplier_iscostumer_supplier_issupplier'),
        ('product', '0009_product_minstock_alter_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
