# Generated by Django 4.2.5 on 2023-10-05 21:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("BookDonations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book_receiver",
            name="drop_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="book_receiver",
            name="school_location",
            field=models.CharField(default="Ikeja", max_length=100),
        ),
        migrations.AddField(
            model_name="book_receiver",
            name="school_name",
            field=models.CharField(default="OGS", max_length=100),
        ),
    ]