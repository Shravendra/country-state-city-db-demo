# Generated by Django 4.1.2 on 2022-10-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0005_city_city_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='state_code',
        ),
        migrations.AddField(
            model_name='state',
            name='state_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
