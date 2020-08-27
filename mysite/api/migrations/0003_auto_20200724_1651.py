# Generated by Django 3.0.8 on 2020-07-24 16:51

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile_no',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]