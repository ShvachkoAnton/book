# Generated by Django 3.1.12 on 2021-06-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knizhki', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
