# Generated by Django 5.0.2 on 2024-02-08 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('num_of_players', models.IntegerField(choices=[(2, 2), (4, 4), (8, 8), (16, 16), (32, 32)], default=2)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(default=None, null=True)),
                ('end_date', models.DateTimeField(default=None, null=True)),
                ('tournament_status', models.CharField(choices=[('waiting', 'Waiting'), ('ongoing', 'Ongoing'), ('complete', 'Complete')], default='waiting', max_length=20)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
