# Generated by Django 4.1.6 on 2023-02-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapiapp', '0002_delete_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisnessprofile',
            name='buisness_images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
