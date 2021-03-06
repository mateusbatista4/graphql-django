# Generated by Django 3.1.4 on 2020-12-05 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('director', models.CharField(max_length=60)),
                ('release_year', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.category')),
            ],
        ),
    ]
