# Generated by Django 5.0.6 on 2024-07-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_taskmanage_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmanage',
            name='detailed_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
