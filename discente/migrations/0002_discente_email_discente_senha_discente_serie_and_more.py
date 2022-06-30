# Generated by Django 4.0.4 on 2022-06-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discente',
            name='email',
            field=models.EmailField(default=50, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discente',
            name='senha',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discente',
            name='serie',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discente',
            name='telefone',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discente',
            name='turma',
            field=models.CharField(default=3, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discente',
            name='usuario',
            field=models.CharField(max_length=50),
        ),
    ]
