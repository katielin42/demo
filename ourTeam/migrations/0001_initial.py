# Generated by Django 3.0.5 on 2020-05-25 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='EELogo_Temp.png', upload_to='picx')),
                ('name', models.CharField(max_length=240)),
                ('position', models.CharField(default='Something Rep.', max_length=240)),
                ('icon', models.CharField(default='fa fa-icon', max_length=240)),
                ('description_1', models.TextField(default='Shall be responsible for ...')),
                ('description_2', models.TextField(default='Shall be responsible for ...')),
                ('description_3', models.TextField(default='Shall be responsible for ...')),
                ('description_4', models.TextField(default='Shall be responsible for ...')),
                ('description_5', models.TextField(default='Shall be responsible for ...')),
                ('email', models.EmailField(max_length=254)),
                ('isSenior', models.BooleanField(default=False)),
                ('isDuplicateDescription', models.BooleanField(default=False)),
            ],
        ),
    ]
