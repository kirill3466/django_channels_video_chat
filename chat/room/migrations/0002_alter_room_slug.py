# Generated by Django 5.0.2 on 2024-02-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(editable=False, null=True, verbose_name='URL'),
        ),
    ]