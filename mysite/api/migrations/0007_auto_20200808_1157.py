# Generated by Django 3.0.8 on 2020-08-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image_name',
            field=models.ImageField(upload_to='polls/static/images'),
        ),
    ]