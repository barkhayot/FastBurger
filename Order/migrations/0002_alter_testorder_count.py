# Generated by Django 4.0 on 2022-01-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorder',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
