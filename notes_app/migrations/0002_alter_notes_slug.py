# Generated by Django 3.2.4 on 2021-06-13 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
