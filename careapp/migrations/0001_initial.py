# Generated by Django 2.2.7 on 2019-12-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('role', models.CharField(max_length=25)),
            ],
        ),
    ]
