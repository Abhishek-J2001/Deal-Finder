# Generated by Django 3.2.16 on 2024-05-29 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Frontend', '0006_rename_user_registerdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldb',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
