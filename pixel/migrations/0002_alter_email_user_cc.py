# Generated by Django 3.2.5 on 2021-07-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='user_cc',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
