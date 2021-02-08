# Generated by Django 3.1.6 on 2021-02-08 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210208_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='design',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='reviews.design'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.process'),
        ),
    ]