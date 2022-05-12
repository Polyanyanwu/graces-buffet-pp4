# Generated by Django 3.2 on 2022-05-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_tables', '0006_diningtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systempreference',
            name='code',
            field=models.CharField(choices=[('D', 'Duration of each Buffet Service'), ('N', 'No Show Time Duration Minutes'), ('C', 'Cancellation Notice Minutes'), ('P', 'Buffet Price per Person'), ('M', 'Max Persons per Online Booking')], default='P', max_length=1, primary_key=True, serialize=False),
        ),
    ]