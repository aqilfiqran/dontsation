# Generated by Django 3.0.5 on 2020-05-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_auto_20200429_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
