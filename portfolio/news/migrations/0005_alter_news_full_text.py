# Generated by Django 4.0.5 on 2022-07-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_group_of_news_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='full_text',
            field=models.TextField(),
        ),
    ]