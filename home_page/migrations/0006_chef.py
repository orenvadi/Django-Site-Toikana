# Generated by Django 4.1.3 on 2022-11-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_rename_adress_map_contact_address_map_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
