# Generated by Django 4.2 on 2023-06-27 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bp_django", "0009_voice_voicebook_voice"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userdialogue",
            old_name="pronounce_score",
            new_name="pronunce_score",
        ),
        migrations.RenameField(
            model_name="voice",
            old_name="sythesis_status",
            new_name="synthesis_status",
        ),
    ]
