# Generated by Django 4.2 on 2023-06-23 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bp_django", "0003_alter_userword_user_alter_userword_word"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userword",
            old_name="pronounce_score",
            new_name="pronunce_score",
        ),
    ]
