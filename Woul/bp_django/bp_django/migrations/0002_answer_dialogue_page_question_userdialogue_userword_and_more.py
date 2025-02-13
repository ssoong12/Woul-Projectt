# Generated by Django 4.2 on 2023-06-23 01:48

import bp_django.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bp_django", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("user_inner_id", models.IntegerField()),
                ("question_inner_id", models.IntegerField()),
                ("title", models.CharField(max_length=50)),
                ("content", models.CharField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Dialogue",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("book_inner_id", models.IntegerField()),
                ("text", models.CharField(max_length=100)),
                ("meaning", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("book_inner_id", models.IntegerField()),
                ("path_to_reading_voice", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("user_inner_id", models.IntegerField()),
                ("title", models.CharField(max_length=50)),
                ("content", models.CharField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserDialogue",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("dialogue_inner_id", models.IntegerField()),
                ("user_inner_id", models.IntegerField()),
                (
                    "pronounce_score",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("path_to_sound", models.CharField(max_length=200)),
                (
                    "dialogue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="userdialogues",
                        to="bp_django.dialogue",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserWord",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("word_inner_id", models.IntegerField()),
                ("user_inner_id", models.IntegerField()),
                (
                    "pronounce_score",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("is_collected", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Voice",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("user_inner_id", models.IntegerField()),
                ("vocal_name", models.CharField(max_length=50)),
                ("path_to_voice_file", models.CharField(max_length=200)),
                (
                    "sythesis_status",
                    models.CharField(
                        max_length=50, validators=[bp_django.models.validate_syn_status]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="VoiceBook",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("voice_inner_id", models.IntegerField()),
                ("book_inner_id", models.IntegerField()),
                ("path_to_synthesized_voice", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Word",
            fields=[
                ("inner_id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("book_inner_id", models.IntegerField()),
                ("text", models.CharField(max_length=50)),
                ("meaning", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name="MyModel",
        ),
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.RemoveField(
            model_name="book",
            name="id",
        ),
        migrations.RemoveField(
            model_name="book",
            name="is_available",
        ),
        migrations.RemoveField(
            model_name="book",
            name="price",
        ),
        migrations.RemoveField(
            model_name="book",
            name="publication_date",
        ),
        migrations.RemoveField(
            model_name="book",
            name="title",
        ),
        migrations.RemoveField(
            model_name="user",
            name="email",
        ),
        migrations.RemoveField(
            model_name="user",
            name="id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="book",
            name="inner_id",
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="name",
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="inner_id",
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="nickname",
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="outer_id",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name="word",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="words",
                to="bp_django.book",
            ),
        ),
        migrations.AddField(
            model_name="voicebook",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voicebooks",
                to="bp_django.book",
            ),
        ),
        migrations.AddField(
            model_name="voicebook",
            name="voice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voicebooks",
                to="bp_django.voice",
            ),
        ),
        migrations.AddField(
            model_name="voice",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voices",
                to="bp_django.user",
            ),
        ),
        migrations.AddField(
            model_name="userword",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userwords",
                to="bp_django.user",
            ),
        ),
        migrations.AddField(
            model_name="userword",
            name="word",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userwords",
                to="bp_django.word",
            ),
        ),
        migrations.AddField(
            model_name="userdialogue",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userdialogues",
                to="bp_django.user",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="bp_django.user",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="bp_django.book",
            ),
        ),
        migrations.AddField(
            model_name="dialogue",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dialogues",
                to="bp_django.book",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="bp_django.question",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="bp_django.user",
            ),
        ),
    ]
