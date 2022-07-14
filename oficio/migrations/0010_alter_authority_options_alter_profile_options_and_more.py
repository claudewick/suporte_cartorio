# Generated by Django 4.0.6 on 2022-07-11 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0009_alter_receivedol_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authority',
            options={'verbose_name': 'Autoridade', 'verbose_name_plural': 'Autoridades'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil de Usuário', 'verbose_name_plural': 'Perfis de Usuários'},
        ),
        migrations.AlterModelOptions(
            name='sentol',
            options={'verbose_name': 'Ofício Enviado', 'verbose_name_plural': 'Ofícios Enviados'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterField(
            model_name='sentol',
            name='accused_doc_number',
            field=models.CharField(max_length=14, null=True, verbose_name='CPF ou CNPJ'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='accused_type',
            field=models.IntegerField(choices=[(1, 'PF'), (2, 'PJ')], default=1, verbose_name='Tipo de Pessoa'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='answer',
            field=models.TextField(verbose_name='Texto do Ofício'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='answer_to_ol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficio.receivedol', verbose_name='Resposta ao Ofício nº'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='author_doc_number',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF ou CNPJ'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='author_type',
            field=models.IntegerField(choices=[(1, 'PF'), (2, 'PJ')], default=1, verbose_name='Tipo de Pessoa'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='authority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficio.authority', verbose_name='Destinatário'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='creation_date',
            field=models.DateField(verbose_name='Data de Eelaboração'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='lawsuit_accused',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Réu'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='lawsuit_author',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='lawsuit_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Processo nº'),
        ),
        migrations.AlterField(
            model_name='sentol',
            name='sent_ol_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de Ofício Expedido'),
        ),
    ]