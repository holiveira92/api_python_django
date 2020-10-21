# Generated by Django 3.0.7 on 2020-06-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Real_Estate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default='1', max_length=1)),
                ('type', models.CharField(choices=[('AP', 'Apartment'), ('HM', 'Home')], default='AP', max_length=2)),
                ('real_estate', models.IntegerField()),
                ('particulars', models.TextField(blank=True, null=True)),
                ('finality', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
