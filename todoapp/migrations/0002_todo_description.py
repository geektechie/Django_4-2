# Generated by Django 4.2.3 on 2023-07-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
