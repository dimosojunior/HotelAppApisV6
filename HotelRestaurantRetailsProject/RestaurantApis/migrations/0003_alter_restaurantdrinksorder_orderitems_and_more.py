# Generated by Django 4.1.3 on 2023-09-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApis', '0002_restaurantdrinksorder_orderitems_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantdrinksorder',
            name='orderItems',
            field=models.ManyToManyField(to='RestaurantApis.restaurantdrinksorderitems'),
        ),
        migrations.AlterField(
            model_name='restaurantfoodorder',
            name='orderItems',
            field=models.ManyToManyField(to='RestaurantApis.restaurantfoodorderitems'),
        ),
    ]
