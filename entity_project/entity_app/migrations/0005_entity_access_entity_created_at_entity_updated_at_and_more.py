# Generated by Django 4.1.5 on 2023-01-26 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("entity_app", "0004_entity_wikidata_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="entity",
            name="access",
            field=models.CharField(
                choices=[("Public", 0), ("Private", 1)], default="Public", max_length=20
            ),
        ),
        migrations.AddField(
            model_name="entity",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="entity",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="entity",
            name="wikidata_id",
            field=models.CharField(editable=False, max_length=16, null=True),
        ),
    ]
