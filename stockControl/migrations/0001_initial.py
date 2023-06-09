# Generated by Django 4.1.7 on 2023-04-13 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0012_product_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Stock insuficiente', max_length=30)),
                ('message', models.CharField(default='Stock insuficiente del producto, por favor, pida más al proveedor', max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
