# Generated by Django 4.1.4 on 2023-01-11 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=30)),
                ('msg', models.CharField(max_length=40)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.contactenquiry')),
            ],
        ),
    ]
