# Generated by Django 3.1.7 on 2021-03-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210225_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='detailed_description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]