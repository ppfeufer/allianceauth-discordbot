# Generated by Django 3.1.1 on 2020-11-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aadiscordbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channels',
            name='channel',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servers',
            name='server',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]