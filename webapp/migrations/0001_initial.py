# Generated by Django 5.0.6 on 2024-06-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], max_length=200, verbose_name='Статус')),
                ('deadline', models.DateField(verbose_name='Дедлайн')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'todo list',
            },
        ),
    ]
