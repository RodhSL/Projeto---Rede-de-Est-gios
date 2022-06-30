# Generated by Django 4.0.4 on 2022-06-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discente', '0005_discente_nome_discente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='discente',
            name='cidade',
            field=models.CharField(max_length=50, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='discente',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='discente',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='discente',
            name='serie',
            field=models.CharField(max_length=10, null=True, verbose_name='Série'),
        ),
        migrations.AddField(
            model_name='discente',
            name='telefone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='discente',
            name='turma',
            field=models.CharField(max_length=10, null=True, verbose_name='Turma'),
        ),
        migrations.AddField(
            model_name='discente',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]