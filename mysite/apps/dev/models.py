from django.db import models
from .choices import *

class Type_devs(models.Model):
    type_dev = models.CharField('Тип оборудования', max_length=200)

    def __str__(self):
        return self.type_dev

    class Meta():
        ordering = ['type_dev']    


class Employes(models.Model):
    surname = models.CharField('Фамилия', max_length=200)
    name = models.CharField('Имя', max_length=200)
    patronymic = models.CharField('Отчество', default = '', max_length=200)
    departament = models.CharField('Департамент', max_length=200)
    position = models.CharField(max_length=200)


    def __str__(self):
        return "%s %s" % (self.surname, self.name)
    
    class Meta():
        ordering = ['id']


class Buildings(models.Model):
    building = models.CharField(max_length=200)
    
    def __str__(self):
        return self.building

    class Meta():
        ordering = ['building']          

class Hardware(models.Model):
    date = models.DateField()
    type_dev = models.ForeignKey(Type_devs, on_delete = models.DO_NOTHING)
    organization = models.CharField('Организация', max_length=200, choices = ORGANIZATION)
    vendor = models.CharField('Производитель', max_length=200, choices = VENDOR)
    model = models.CharField('Модель', max_length=200)
    serial_number = models.CharField('Серийный номер', max_length=200, unique=True)
    inv_number = models.CharField('Инвентарный номер', max_length=200, null=True, blank=True)
    status = models.CharField('Статус', max_length=200, choices = STATUS)
    buildings = models.ForeignKey(Buildings, on_delete = models.DO_NOTHING)
    room = models.CharField('Помещение', max_length=200)
    employ = models.ForeignKey(Employes, blank = True, on_delete=models.DO_NOTHING)
    note = models.CharField('Заметка', max_length=500, null=True, blank=True)
    seller = models.CharField('Поставщик', max_length=200, choices = SELLER, null=True, blank=True)
    date_of_sale = models.CharField('Дата покупки', max_length=200, null=True, blank=True)
    MOL = models.CharField('МОЛ', max_length=200, choices = MOL)
    
    def __str__(self):
        return self.organization

    class Meta():
        ordering = ['-date']
        
class Printers(models.Model):
    name_printers = models.CharField('Имя принтера', max_length=200, default='')
    IP = models.CharField('IP адрес', max_length=200, default='')
    type_printers = models.CharField('Тип принтера', max_length=200, choices=PRINTERS)
    
    def __str__(self):
        return self.name_printers