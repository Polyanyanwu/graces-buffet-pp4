# Generated by Django 3.2 on 2022-05-14 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general_tables', '0007_alter_systempreference_code'),
        ('bookings', '0007_auto_20220514_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked_for', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_tables.bookingstatus'),
        ),
    ]
