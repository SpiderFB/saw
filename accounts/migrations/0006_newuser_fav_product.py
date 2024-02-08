# Generated by Django 4.2.2 on 2024-02-07 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('accounts', '0005_newuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='fav_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productdb'),
        ),
    ]
