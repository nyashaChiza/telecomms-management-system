# Generated by Django 5.0.6 on 2024-05-25 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0004_license_location_alter_license_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]