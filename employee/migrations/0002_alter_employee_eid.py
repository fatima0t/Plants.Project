# Generated by Django 4.1.7 on 2023-05-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=15),
        ),
    ]
