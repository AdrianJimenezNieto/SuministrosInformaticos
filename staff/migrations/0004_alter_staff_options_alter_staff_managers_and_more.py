# Generated by Django 4.1.7 on 2023-03-26 13:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0003_remove_staff_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='staff',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='staff',
            name='dateSingUp',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='id',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='ident',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
        migrations.AddField(
            model_name='staff',
            name='idcard',
            field=models.CharField(default='00000000X', max_length=10),
        ),
        migrations.AddField(
            model_name='staff',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='cp',
            field=models.CharField(max_length=10),
        ),
    ]
