# Generated by Django 4.0.6 on 2022-07-11 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0008_alter_receivedol_accused_doc_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receivedol',
            options={'verbose_name': 'Ofício Recebido', 'verbose_name_plural': 'Ofícios Recebidos'},
        ),
    ]
