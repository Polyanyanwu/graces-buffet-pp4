# Generated by Django 3.2 on 2022-05-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_auto_20220515_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablesbooked',
            name='time_booked',
            field=models.TimeField(null=True),
        ),
    ]
