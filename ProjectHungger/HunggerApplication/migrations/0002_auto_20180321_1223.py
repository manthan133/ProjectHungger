# Generated by Django 2.0.2 on 2018-03-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HunggerApplication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.CharField(default='user', max_length=200),
        ),
        migrations.AlterField(
            model_name='cart',
            name='food_id',
            field=models.IntegerField(default=0),
        ),
    ]
