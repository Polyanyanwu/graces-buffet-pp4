# Generated by Django 3.2 on 2022-05-13 14:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_booking_dinner_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dinner_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
