# Generated by Django 3.1.2 on 2021-01-25 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_auto_20210124_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='buyed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyed', to='shop_app.productname'),
        ),
        migrations.AlterField(
            model_name='productname',
            name='product_price',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
