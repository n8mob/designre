# Generated by Django 3.1.6 on 2021-02-08 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.process')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.step')),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='steps',
            field=models.ManyToManyField(through='reviews.ProcessStep', to='reviews.Step'),
        ),
    ]
