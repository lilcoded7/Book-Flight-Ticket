# Generated by Django 4.2.4 on 2023-08-11 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=100)),
                ('passenger_email', models.EmailField(max_length=254)),
                ('flight_number', models.CharField(max_length=10)),
                ('departure_city', models.CharField(max_length=100)),
                ('arrival_city', models.CharField(max_length=100)),
                ('departure_date', models.DateField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking_reference', models.CharField(max_length=8, unique=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]