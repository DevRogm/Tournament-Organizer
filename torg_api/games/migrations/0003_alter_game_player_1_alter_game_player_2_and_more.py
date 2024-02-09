# Generated by Django 5.0.2 on 2024-02-09 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_score_1_game_score_2_game_winner'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_1', to='players.player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_2', to='players.player'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_1',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_2',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
