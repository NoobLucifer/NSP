# Generated by Django 2.0.1 on 2018-06-14 03:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50)),
                ('mentor_name', models.CharField(default='', max_length=50)),
                ('branch', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(max_length=2500)),
                ('paid', models.BooleanField(default=False)),
                ('start_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField(default=0, null=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('year', models.IntegerField(null=True)),
                ('branch', models.CharField(blank=True, default='', max_length=20)),
                ('stream', models.CharField(blank=True, default='', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounts_userprofile',
            },
        ),
    ]
