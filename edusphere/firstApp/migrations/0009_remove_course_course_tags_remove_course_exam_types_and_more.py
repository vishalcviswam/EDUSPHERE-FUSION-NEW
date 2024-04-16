# Generated by Django 5.0a1 on 2023-11-01 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0008_remove_course_course_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_tags',
        ),
        migrations.RemoveField(
            model_name='course',
            name='exam_types',
        ),
        migrations.RemoveField(
            model_name='course',
            name='languages',
        ),
        migrations.AddField(
            model_name='course',
            name='course_tags',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='course',
            name='exam_types',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='course',
            name='languages',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
