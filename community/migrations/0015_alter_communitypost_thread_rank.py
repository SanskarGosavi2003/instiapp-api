# Generated by Django 3.2.13 on 2022-07-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_alter_communitypost_thread_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='thread_rank',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
