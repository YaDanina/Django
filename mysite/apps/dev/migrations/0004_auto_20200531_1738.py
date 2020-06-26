# Generated by Django 3.0.6 on 2020-05-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0003_printers'),
    ]

    operations = [
        migrations.AddField(
            model_name='printers',
            name='type_printers',
            field=models.CharField(choices=[('ПРИНТЕР', 'ПРИНТЕР'), ('МФУ', 'МФУ'), ('ПЛОТТЕР', 'ПЛОТТЕР')], default='', max_length=200, verbose_name='Тип принтера'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='printers',
            name='IP',
            field=models.CharField(default='', max_length=200, verbose_name='IP адрес'),
        ),
        migrations.AlterField(
            model_name='printers',
            name='name_printers',
            field=models.CharField(default='', max_length=200, verbose_name='Имя принтера'),
        ),
    ]
