# Generated by Django 4.1 on 2023-07-06 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp', '0005_alter_observation_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='bird_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='observation',
            old_name='bird_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='observation_date',
        ),
        migrations.AddField(
            model_name='observation',
            name='date',
            field=models.DateField(default='1900-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='observation',
            name='picture',
            field=models.ImageField(default='static/images/profile.jpeg', upload_to='static/images', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
