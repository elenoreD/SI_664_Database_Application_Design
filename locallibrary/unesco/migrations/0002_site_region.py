# Generated by Django 2.2.5 on 2019-09-24 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='unesco.Region'),
            preserve_default=False,
        ),
    ]