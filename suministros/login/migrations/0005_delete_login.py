# Generated by Django 4.1.7 on 2023-03-17 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_login_accesslevel_remove_login_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]