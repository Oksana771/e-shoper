# Generated by Django 3.1.3 on 2020-12-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20201222_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
