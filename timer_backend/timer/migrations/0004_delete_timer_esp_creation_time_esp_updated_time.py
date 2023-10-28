# Generated by Django 4.2.6 on 2023-10-28 23:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("timer", "0003_rename_time_esp_timer"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Timer",
        ),
        migrations.AddField(
            model_name="esp",
            name="creation_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="esp",
            name="updated_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]