# Generated by Django 4.0.3 on 2022-03-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisitorLog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]