# Generated by Django 3.0.8 on 2020-07-23 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200723_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
