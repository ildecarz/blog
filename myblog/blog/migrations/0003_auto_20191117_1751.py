# Generated by Django 2.2.7 on 2019-11-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191117_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.TextField(max_length=50),
        ),
    ]
