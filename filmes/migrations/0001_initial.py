# Generated by Django 4.2.6 on 2023-11-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('generos', models.JSONField()),
                ('streamings', models.JSONField()),
                ('links', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
                ('favoritos', models.ManyToManyField(to='filmes.filme')),
            ],
        ),
    ]
