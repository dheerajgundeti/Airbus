# Generated by Django 2.2.1 on 2019-12-08 08:13

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Airbus', '0002_auto_20191208_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('user', models.CharField(max_length=20)),
                ('profile_picture', models.TextField()),
                ('full_post', models.TextField()),
            ],
        ),
    ]
