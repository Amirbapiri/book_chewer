# Generated by Django 3.1.7 on 2021-04-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='experience',
            field=models.SmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Expert')], default=0),
        ),
    ]
