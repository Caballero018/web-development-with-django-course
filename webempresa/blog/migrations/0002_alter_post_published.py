# Generated by Django 4.2.15 on 2024-09-01 23:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Fecha de publicación"
            ),
        ),
    ]
