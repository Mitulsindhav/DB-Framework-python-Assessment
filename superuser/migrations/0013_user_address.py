# Generated by Django 5.1.6 on 2025-04-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0012_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
