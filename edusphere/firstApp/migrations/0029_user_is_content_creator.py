# Generated by Django 5.0a1 on 2024-02-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0028_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_content_creator',
            field=models.BooleanField(default=False),
        ),
    ]
