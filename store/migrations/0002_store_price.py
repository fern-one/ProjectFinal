# Generated by Django 4.0 on 2022-03-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
