# Generated by Django 4.1.7 on 2023-03-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0004_alter_costumer_options_alter_costumer_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumer',
            name='accessLevel',
        ),
        migrations.AddField(
            model_name='costumer',
            name='adress',
            field=models.CharField(default='No adress', max_length=20),
        ),
        migrations.AddField(
            model_name='costumer',
            name='cp',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]