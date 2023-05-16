# Generated by Django 4.2.1 on 2023-05-13 12:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.PositiveIntegerField(default=300, validators=[django.core.validators.MaxValueValidator(limit_value=9999, message='Максимальный вес 9999г.')], verbose_name='Вес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=9999, message='Максимальная цена 9999р.')], verbose_name='Цена'),
        ),
    ]