# Generated by Django 2.0.2 on 2019-12-14 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191215_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
