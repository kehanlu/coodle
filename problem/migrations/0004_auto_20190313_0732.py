# Generated by Django 2.1.5 on 2019-03-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_auto_20190312_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='sample_code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='short_description',
            field=models.TextField(blank=True),
        ),
    ]
