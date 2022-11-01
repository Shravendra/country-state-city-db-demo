# Generated by Django 4.1.2 on 2022-10-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_country_country_id_state_state_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='state_code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
