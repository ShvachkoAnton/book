# Generated by Django 3.1.12 on 2021-06-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knizhki', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special status', 'can read all books')]},
        ),
    ]