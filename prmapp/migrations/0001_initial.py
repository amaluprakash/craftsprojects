# Generated by Django 4.0.3 on 2023-06-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default='0', upload_to='')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=40)),
            ],
        ),
    ]
