# Generated by Django 4.0.5 on 2022-07-06 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_messagesforus_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagesforus',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterField(
            model_name='messagesforus',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 6, 10, 52, 48, 671710), verbose_name='data'),
        ),
    ]
