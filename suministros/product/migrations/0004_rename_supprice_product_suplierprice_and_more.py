# Generated by Django 4.1.7 on 2023-03-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_categoria_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='supPrice',
            new_name='suplierPrice',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.FloatField(),
        ),
    ]
