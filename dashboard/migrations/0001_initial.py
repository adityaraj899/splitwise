# Generated by Django 2.0.2 on 2018-06-20 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=128)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Category'),
        ),
        migrations.AddField(
            model_name='bill',
            name='paidby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Friends'),
        ),
    ]