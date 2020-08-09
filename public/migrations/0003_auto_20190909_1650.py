# Generated by Django 2.1.11 on 2019-09-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20190909_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=80, null=True)),
                ('hostip', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='groups',
            name='hostList',
            field=models.ManyToManyField(to='public.Hosts'),
        ),
    ]
