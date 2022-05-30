# Generated by Django 4.0.4 on 2022-05-01 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0010_movie_seriestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSurname', models.CharField(max_length=30, verbose_name='Yorum Yapan Kişi')),
                ('mesaj', models.CharField(max_length=500, verbose_name='Yapılan Yorum')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yorum Yapılan Tarih')),
                ('movieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movieComment', to='movieapp.movie')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'Yorumlar',
                'db_table': 'tblcomment',
            },
        ),
    ]