# Generated by Django 4.2.4 on 2023-09-01 12:26

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_blog_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]
