# Generated by Django 4.2.2 on 2023-07-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp', '0004_alter_observation_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='picture',
            field=models.ImageField(default='static/images/profile.jpeg', upload_to='static/images'),
        ),
    ]