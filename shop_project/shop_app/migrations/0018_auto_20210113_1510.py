# Generated by Django 3.1.2 on 2021-01-13 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0017_auto_20210113_0150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productname',
            old_name='product_instance_category',
            new_name='product_object_category',
        ),
        migrations.RenameField(
            model_name='productname',
            old_name='product_instance_description',
            new_name='product_object_description',
        ),
        migrations.RenameField(
            model_name='productname',
            old_name='product_instance_name',
            new_name='product_object_name',
        ),
    ]