# Generated by Django 3.2.12 on 2024-07-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icoderApp', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='subtitle',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
    ]
