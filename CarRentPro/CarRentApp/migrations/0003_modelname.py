# Generated by Django 3.0.2 on 2020-02-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentApp', '0002_maciek'),
    ]

    operations = [
        migrations.CreateModel(
            name='MODELNAME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('klasa', models.CharField(max_length=50)),
            ],
        ),
    ]
