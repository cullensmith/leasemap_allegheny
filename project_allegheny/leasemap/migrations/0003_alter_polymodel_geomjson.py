# Generated by Django 5.1 on 2024-11-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasemap', '0002_polymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polymodel',
            name='geomjson',
            field=models.CharField(max_length=250),
        ),
    ]
