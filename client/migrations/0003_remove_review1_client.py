# Generated by Django 4.1.4 on 2023-03-14 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review1',
            name='client',
        ),
    ]
