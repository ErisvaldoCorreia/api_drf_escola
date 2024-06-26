# Generated by Django 3.0.7 on 2024-06-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=9)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('codigo', models.CharField(choices=[('B', 'Basico'), ('I', 'Intermediario'), ('A', 'Avancado')], default='B', max_length=1)),
            ],
        ),
    ]
