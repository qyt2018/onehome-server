# Generated by Django 2.1.2 on 2018-10-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20181007_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_image_URL',
            field=models.ImageField(null=True, upload_to='static/userImages'),
        ),
    ]
