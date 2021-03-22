# Generated by Django 3.1.6 on 2021-03-22 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20210215_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questionnaire.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questionnaire.test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='solved',
            field=models.IntegerField(default=0, verbose_name='solved'),
        ),
    ]