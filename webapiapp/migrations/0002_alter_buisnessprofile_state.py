# Generated by Django 4.1.6 on 2023-02-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisnessprofile',
            name='state',
            field=models.CharField(blank=True, choices=[('1', 'abia'), ('2', 'adamawa'), ('3', 'akwa ibom'), ('4', 'anambra'), ('5', 'bauchi'), ('6', 'bayelsa'), ('7', 'benue'), ('8', 'borno '), ('9', 'cross river'), ('10', 'delta'), ('11', 'ebonyi'), ('12', 'edo'), ('13', 'ekiti'), ('14', 'enugu'), ('15', 'gombe'), ('16', 'imo'), ('17', 'jigawa'), ('18', 'kaduna'), ('19', 'kano'), ('20', 'katsina'), ('21', 'kebbi'), ('22', 'kogi'), ('23', 'kwara'), ('24', 'lagos'), ('25', 'nasarawa'), ('26', 'niger'), ('27', 'ogun'), ('28', 'ondo'), ('29', 'osun'), ('30', 'oyo'), ('31', 'plateau'), ('32', 'rivers'), ('33', 'sokoto'), ('34', 'taraba'), ('35', 'yobe '), ('36', 'zamfara')], max_length=50),
        ),
    ]
