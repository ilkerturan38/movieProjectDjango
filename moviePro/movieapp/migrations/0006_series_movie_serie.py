# Generated by Django 4.0.4 on 2022-04-29 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_alter_person_namesurname'),
    ]

    operations = [
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Serinin Adı')),
            ],
            options={
                'verbose_name': 'series',
                'verbose_name_plural': 'Seriler',
                'db_table': 'tblseries',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='serie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seriesMovie', to='movieapp.series'),
        ),
    ]
