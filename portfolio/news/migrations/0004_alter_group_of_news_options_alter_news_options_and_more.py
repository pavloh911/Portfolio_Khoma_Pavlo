# Generated by Django 4.0.5 on 2022-07-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_author_img_alter_news_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group_of_news',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]