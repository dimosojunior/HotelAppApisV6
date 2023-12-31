# Generated by Django 4.1.3 on 2023-09-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApis', '0006_remove_hotelstorebincode_storecode'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelEventCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=500, verbose_name='Code')),
                ('Description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hotel Event Code',
            },
        ),
    ]
