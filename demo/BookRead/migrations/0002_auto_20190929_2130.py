# Generated by Django 2.2.1 on 2019-09-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookRead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='email',
            field=models.TextField(),
        ),
    ]
