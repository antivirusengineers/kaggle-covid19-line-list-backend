# Generated by Django 2.2.11 on 2020-03-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]