# Generated by Django 3.0.5 on 2020-05-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourTeam', '0010_auto_20200519_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='isSenior',
            field=models.BooleanField(default=False),
        ),
    ]
