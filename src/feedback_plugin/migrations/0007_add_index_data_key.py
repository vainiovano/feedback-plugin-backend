# Generated by Django 4.1.2 on 2023-03-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_plugin', '0006_add_index_to_facts'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='data',
            index=models.Index(fields=['upload', 'key'], name='feedback_pl_upload__bfa44e_idx'),
        ),
    ]