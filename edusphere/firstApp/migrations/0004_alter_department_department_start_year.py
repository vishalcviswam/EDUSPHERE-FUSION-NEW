# Generated by Django 5.0a1 on 2023-10-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_start_year',
            field=models.DateField(),
        ),
    ]
