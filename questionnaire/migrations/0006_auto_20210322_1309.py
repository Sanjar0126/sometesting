# Generated by Django 3.1.6 on 2021-03-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_auto_20210322_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='solved',
            field=models.IntegerField(default=0),
        ),
    ]
