# Generated by Django 4.0.4 on 2022-05-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0028_remove_movie_image_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_quality',
            field=models.CharField(blank=True, choices=[('1', '4K'), ('2', '1080P'), ('3', '720P'), ('4', '480P')], max_length=1, null=True, verbose_name='Görüntü Kalitesi'),
        ),
    ]