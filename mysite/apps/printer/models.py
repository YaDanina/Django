from django.db import models




class Printers_Stat(models.Model):
    date = models.DateField()
    serial_number = models.CharField('Серийный номер', unique=True, max_length=200)
    name_printers = models.CharField('Имя принтера', max_length=200)
    ip_address =  models.CharField('IP адрес', max_length=200)
    type_printers = models.CharField('Тип принтера', max_length=200)
    page_count = models.CharField('Количество отпечатанных страниц', max_length=200)
    capacity_toner_black = models.CharField('Емкость Черный', max_length=200)
    toner_count_black = models.CharField('Черный', max_length=200)
    capacity_toner_cyan = models.CharField('Емкость Синий', max_length=200, default='')
    toner_count_cyan = models.CharField('Синий', max_length=200, default='')
    capacity_toner_magenta = models.CharField('Емкость Красный', max_length=200, default='')
    toner_count_magenta = models.CharField('Красный', max_length=200, default='')
    capacity_toner_yellow = models.CharField('Емкость Желтый', max_length=200, default='')
    toner_count_yellow = models.CharField('Желтый', max_length=200, default='')
    cartridge_type = models.CharField('Тип картриджа', max_length=200, default='')

    def __str__(self):
        return self.name_printers

    class Meta():
        ordering = ['-date']


class Printer_Color(models.Model):
    datetime = models.DateTimeField()
    name_printers = models.CharField('Имя принтера', max_length=200)
    toner_black = models.IntegerField('Черный', max_length=200)
    toner_cyan = models.IntegerField('Синий', max_length=200)
    toner_magenta = models.IntegerField('Красный', max_length=200)
    toner_yellow = models.IntegerField('Желтый', max_length=200)

    class Meta():
        ordering = ['-datetime']
    
    def __str__(self):
        return self.name_printers


