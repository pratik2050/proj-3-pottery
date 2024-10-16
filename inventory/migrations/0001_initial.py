# Generated by Django 5.1.2 on 2024-10-12 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('from_person', models.CharField(max_length=200)),
                ('monument', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_stage', models.CharField(max_length=50)),
                ('to_stage', models.CharField(max_length=50)),
                ('transferred_quantity', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('monument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.monument')),
            ],
        ),
    ]