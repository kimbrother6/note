# Generated by Django 2.2 on 2021-05-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='Memorization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='english_sentence',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='korean_sentence',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
