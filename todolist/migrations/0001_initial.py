# Generated by Django 5.1.7 on 2025-03-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
