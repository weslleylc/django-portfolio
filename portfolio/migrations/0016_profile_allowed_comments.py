<<<<<<< HEAD
# Generated by Django 3.0.7 on 2020-06-21 03:16
=======
# Generated by Django 3.0.7 on 2020-06-21 03:15
>>>>>>> 5d723ebddd2ca1ab5ab9e6dbb586e70d3ce9e1e9

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20200620_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='allowed_comments',
            field=models.BooleanField(default=False),
        ),
    ]
