# Generated by Django 3.1.7 on 2021-03-01 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_article_detailed_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
    ]
