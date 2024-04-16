# Generated by Django 4.2.5 on 2024-02-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0037_community_message_communitymembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='community_covers/'),
        ),
        migrations.AddField(
            model_name='community',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='community_profiles/'),
        ),
        migrations.AddField(
            model_name='community',
            name='rules',
            field=models.TextField(blank=True, null=True),
        ),
    ]
