# Generated by Django 4.2.1 on 2023-06-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='Email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
