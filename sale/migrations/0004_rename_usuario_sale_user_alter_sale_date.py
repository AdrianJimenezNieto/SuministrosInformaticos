# Generated by Django 4.1.7 on 2023-03-30 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_sale_amount_sale_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='usuario',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 30)),
        ),
    ]