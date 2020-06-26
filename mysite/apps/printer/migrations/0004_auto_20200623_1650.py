# Generated by Django 3.0.6 on 2020-06-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0003_printers_stat_cartridge_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='printers_stat',
            name='capacity_toner_black',
            field=models.CharField(default='', max_length=200, verbose_name='Емкость Черный'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='capacity_toner_cyan',
            field=models.CharField(default='', max_length=200, verbose_name='Емкость Синий'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='capacity_toner_magenta',
            field=models.CharField(default='', max_length=200, verbose_name='Емкость Красный'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='capacity_toner_yellow',
            field=models.CharField(default='', max_length=200, verbose_name='Емкость Желтый'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='ip_address',
            field=models.CharField(default='', max_length=200, verbose_name='IP адрес'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='name_printers',
            field=models.CharField(default='', max_length=200, verbose_name='Имя принтера'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='page_count',
            field=models.CharField(default='', max_length=200, verbose_name='Количество отпечатанных страниц'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='serial_number',
            field=models.CharField(default='', max_length=200, unique=True, verbose_name='Серийный номер'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='toner_count_black',
            field=models.CharField(default='', max_length=200, verbose_name='Черный'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='toner_count_cyan',
            field=models.CharField(default='', max_length=200, verbose_name='Синий'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='toner_count_magenta',
            field=models.CharField(default='', max_length=200, verbose_name='Красный'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='toner_count_yellow',
            field=models.CharField(default='', max_length=200, verbose_name='Желтый'),
        ),
        migrations.AddField(
            model_name='printers_stat',
            name='type_printers',
            field=models.CharField(default='', max_length=200, verbose_name='Тип принтера'),
        ),
    ]
