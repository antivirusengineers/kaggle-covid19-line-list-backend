# Generated by Django 2.2.11 on 2020-03-30 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('death', models.BooleanField(default=False)),
                ('recovered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.Case')),
            ],
            options={
                'unique_together': {('case', 'name')},
            },
        ),
    ]
