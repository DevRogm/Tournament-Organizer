# Generated by Django 5.0.2 on 2024-02-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_is_approved_alter_game_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_num',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
