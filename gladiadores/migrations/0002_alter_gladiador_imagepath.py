# Generated by Django 5.1.3 on 2024-12-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gladiadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gladiador',
            name='imagePath',
            field=models.BinaryField(),
        ),
    ]
