# Generated by Django 3.0.8 on 2020-07-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('mobile_no', models.CharField(max_length=14)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
