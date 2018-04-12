# Generated by Django 2.0.2 on 2018-03-21 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HunggerApplication', '0002_auto_20180321_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HunggerApplication.food'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HunggerApplication.user'),
        ),
    ]