# Generated by Django 5.0.2 on 2024-03-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=10),
        ),
    ]