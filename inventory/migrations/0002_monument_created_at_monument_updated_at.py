# Generated by Django 5.1.2 on 2024-10-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monument',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='monument',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
