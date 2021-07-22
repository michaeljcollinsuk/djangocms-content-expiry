# Generated by Django 2.2.24 on 2021-07-22 10:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentExpiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ContentExpiryContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_expiry_date', models.DateField(default=datetime.date.today, verbose_name='From Expiry Date')),
                ('to_expiry_date', models.DateField(default=datetime.date.today, verbose_name='To Expiry Date')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Content Expiry',
            },
        ),
    ]
