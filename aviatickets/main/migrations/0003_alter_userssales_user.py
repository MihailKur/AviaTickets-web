# Generated by Django 4.1.7 on 2023-03-14 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_tickets_name_dest_alter_tickets_name_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userssales',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
