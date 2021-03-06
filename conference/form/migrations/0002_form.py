# Generated by Django 3.2 on 2021-05-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=128)),
                ('user_id', models.CharField(max_length=128)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('day', models.CharField(max_length=128)),
                ('time_id', models.IntegerField(blank=True, null=True)),
                ('Participants', models.CharField(max_length=128)),
                ('statu', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'Form',
            },
        ),
    ]
