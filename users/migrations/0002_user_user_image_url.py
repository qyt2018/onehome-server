# Generated by Django 2.1.2 on 2018-10-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image_URL',
            field=models.ImageField(null=True, upload_to='static/userImages'),
        ),
    ]
