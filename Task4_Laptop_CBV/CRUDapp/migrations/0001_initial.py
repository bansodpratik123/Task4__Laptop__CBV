# Generated by Django 3.2.7 on 2021-09-15 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model_Name', models.CharField(max_length=32)),
                ('Company', models.CharField(max_length=32)),
                ('RAM', models.IntegerField()),
                ('ROM', models.IntegerField()),
                ('Processor', models.CharField(max_length=32)),
                ('Weight', models.FloatField()),
                ('Price', models.FloatField()),
            ],
        ),
    ]
