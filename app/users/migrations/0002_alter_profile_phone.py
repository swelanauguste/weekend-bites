# Generated by Django 4.2.3 on 2023-07-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='+1', max_length=20, null=True),
        ),
    ]