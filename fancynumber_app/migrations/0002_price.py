# Generated by Django 4.2.1 on 2024-02-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fancynumber_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
