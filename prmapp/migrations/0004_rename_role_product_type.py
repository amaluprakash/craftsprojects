# Generated by Django 4.0.3 on 2023-06-26 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prmapp', '0003_rename_models_product_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='role',
            new_name='type',
        ),
    ]
