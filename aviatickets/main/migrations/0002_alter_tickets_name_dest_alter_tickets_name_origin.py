# Generated by Django 4.1.7 on 2023-03-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='name_dest',
            field=models.CharField(choices=[('Москва', 'Москва'), ('Екатеринбург', 'Екатеринбург'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Нижний Новгород', 'Нижний Новгород'), ('Астана', 'Астана'), ('Сочи', 'Сочи')], max_length=100, verbose_name='Город прилета'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='name_origin',
            field=models.CharField(choices=[('Москва', 'Москва'), ('Екатеринбург', 'Екатеринбург'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Нижний Новгород', 'Нижний Новгород'), ('Астана', 'Астана'), ('Сочи', 'Сочи')], max_length=100, verbose_name='Город вылета'),
        ),
    ]
