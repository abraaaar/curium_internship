# Generated by Django 5.0.1 on 2024-01-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('five', '0006_alter_userdetails_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
