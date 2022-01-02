# Generated by Django 4.0 on 2022-01-02 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_alter_testorder_order_t'),
    ]

    operations = [
        migrations.AddField(
            model_name='testorder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]