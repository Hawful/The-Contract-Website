# Generated by Django 2.2.13 on 2021-04-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shown_fiction', models.TextField(max_length=30000)),
                ('hidden_fiction', models.TextField(max_length=30000)),
            ],
        ),
    ]
