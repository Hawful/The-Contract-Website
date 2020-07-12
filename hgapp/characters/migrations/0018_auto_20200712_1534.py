# Generated by Django 2.2.12 on 2020-07-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0017_auto_20200712_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactertutorial',
            name='exert_body',
            field=models.TextField(default='You may Exert your body before rolling for a physical action to gain an automatic success or to ignore your Penalty for that action. Exertion results in a new Severity-y-one Injury.', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charactertutorial',
            name='exert_mind',
            field=models.TextField(default='You may Exert your mind to activate a Power, or before rolling for a mental action to gain an automatic success or to ignore your Penalty for that action. Exertion results in one level of Mind damage.', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charactertutorial',
            name='recover_mind',
            field=models.TextField(default='Mind recovers at the rate of one level per day and requires a long and restful sleep.', max_length=3000),
            preserve_default=False,
        ),
    ]
