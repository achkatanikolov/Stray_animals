# Generated by Django 3.1.7 on 2021-03-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='animal_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
