# Generated by Django 4.0.4 on 2022-05-09 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0024_serialvideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serialvideo',
            old_name='movie',
            new_name='serial',
        ),
    ]