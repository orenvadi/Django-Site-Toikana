# Generated by Django 4.1.4 on 2022-12-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_rename_guests_num_booking_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(choices=[('First courses', 'First courses'), ('Second courses', 'Second courses'), ('Desserts', 'Desserts'), ('Wine Map', 'Wine Map'), ('Drinks', 'Drinks')], max_length=100),
        ),
    ]
