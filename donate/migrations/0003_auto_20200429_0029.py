# Generated by Django 3.0.5 on 2020-04-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_remove_donate_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='barcode',
            field=models.CharField(max_length=200, verbose_name='Code'),
        ),
    ]