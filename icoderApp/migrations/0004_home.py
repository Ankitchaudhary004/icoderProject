# Generated by Django 3.2.12 on 2024-07-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icoderApp', '0003_auto_20240704_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('subtitle', models.CharField(default='', max_length=300)),
                ('button', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='static/index')),
            ],
        ),
    ]
