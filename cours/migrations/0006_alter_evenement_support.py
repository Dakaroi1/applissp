# Generated by Django 4.2.2 on 2023-09-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0005_evenement_rename_titre_cours_cours_titre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='Support',
            field=models.FileField(upload_to='media/'),
        ),
    ]
