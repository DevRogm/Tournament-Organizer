# Generated by Django 5.0.2 on 2024-02-18 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_game_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_num',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(16)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_round',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_1',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_2',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
    ]