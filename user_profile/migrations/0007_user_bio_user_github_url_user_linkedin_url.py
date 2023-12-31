# Generated by Django 4.2.4 on 2023-08-28 12:29

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0006_remove_socialmedialink_platform_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="github_url",
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="linkedIn_url",
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
