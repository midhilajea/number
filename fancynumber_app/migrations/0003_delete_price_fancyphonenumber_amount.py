# Generated by Django 4.2.1 on 2024-02-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fancynumber_app', '0002_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='fancyphonenumber',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
