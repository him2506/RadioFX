# Generated by Django 3.0.6 on 2020-08-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=600)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('category', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('Language', models.CharField(default='', max_length=100)),
                ('top', models.BooleanField(default=False)),
                ('Pop', models.BooleanField(default=False)),
                ('Rock', models.BooleanField(default=False)),
                ('Electronic', models.BooleanField(default=False)),
                ('Hip_Hop', models.BooleanField(default=False)),
                ('Classic', models.BooleanField(default=False)),
                ('Dance', models.BooleanField(default=False)),
                ('LoveSongs', models.BooleanField(default=False)),
                ('OldSongs', models.BooleanField(default=False)),
                ('UnpluggedSongs', models.BooleanField(default=False)),
            ],
        ),
    ]
