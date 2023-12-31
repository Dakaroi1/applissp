# Generated by Django 4.2.2 on 2023-09-06 23:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0004_cours_consultation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('Support', models.FileField(upload_to='pdfs/')),
                ('Auteur', models.CharField(max_length=100)),
                ('Classe_auteur', models.CharField(default=' ', max_length=100)),
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
                ('Date_actualisation', models.DateTimeField(auto_now=True)),
                ('Consultation', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='cours',
            old_name='Titre_cours',
            new_name='Titre',
        ),
        migrations.AddField(
            model_name='cours',
            name='Classe_auteur',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cours',
            name='Matiere_concerné',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cours',
            name='Type_document',
            field=models.CharField(choices=[('option1', 'Cours'), ('option2', 'Exercices'), ('option3', 'Corrections')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cours',
            name='Auteur',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Consulter',
        ),
    ]
