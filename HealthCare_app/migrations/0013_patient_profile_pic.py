# Generated by Django 3.0.5 on 2020-05-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCare_app', '0012_auto_20200523_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/'),
        ),
    ]
