# Generated by Django 4.2.1 on 2023-08-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_student_createddate_student_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Studentname',
            field=models.CharField(max_length=52),
        ),
    ]
