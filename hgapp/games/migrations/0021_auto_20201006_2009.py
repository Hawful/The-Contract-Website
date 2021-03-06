# Generated by Django 2.2.13 on 2020-10-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_auto_20201005_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioTag',
            fields=[
                ('tag', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=40, primary_key=True, serialize=False, verbose_name='Unique URL-Safe Name')),
            ],
        ),
        migrations.AlterField(
            model_name='scenario_discovery',
            name='reason',
            field=models.CharField(choices=[('PLAYED', 'Played'), ('CREATED', 'Created'), ('SHARED', 'Shared'), ('UNLOCKED', 'Unlocked')], max_length=25),
        ),
        migrations.AddField(
            model_name='scenario',
            name='tags',
            field=models.ManyToManyField(blank=True, to='games.ScenarioTag'),
        ),
    ]
