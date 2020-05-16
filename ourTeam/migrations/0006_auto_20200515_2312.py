# Generated by Django 3.0.5 on 2020-05-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourTeam', '0005_auto_20200515_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='description',
        ),
        migrations.AddField(
            model_name='team',
            name='description_1',
            field=models.TextField(default='Shall be responsible for ...'),
        ),
        migrations.AddField(
            model_name='team',
            name='description_2',
            field=models.TextField(default='Shall be responsible for ...'),
        ),
        migrations.AddField(
            model_name='team',
            name='description_3',
            field=models.TextField(default='Shall be responsible for ...'),
        ),
        migrations.AddField(
            model_name='team',
            name='description_4',
            field=models.TextField(default='Shall be responsible for ...'),
        ),
        migrations.AddField(
            model_name='team',
            name='description_5',
            field=models.TextField(default='Shall be responsible for ...'),
        ),
        migrations.AddField(
            model_name='team',
            name='id_name',
            field=models.CharField(default='somethingrep', max_length=25),
        ),
        migrations.AddField(
            model_name='team',
            name='lessfunc',
            field=models.TextField(default="'return less('<id>');'"),
        ),
        migrations.AddField(
            model_name='team',
            name='morefunc',
            field=models.TextField(default="'return more('<id>');'"),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(default='Something Rep.', max_length=21),
        ),
    ]