# Generated by Django 3.0.8 on 2020-07-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image1',
            field=models.ImageField(default='images/bear.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(default='images/bear.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(default='images/bear.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='images/bear.png', upload_to=''),
        ),
    ]
