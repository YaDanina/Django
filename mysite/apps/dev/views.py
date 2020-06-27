import os
from django.shortcuts import render, redirect
from .models import *
from printer.models import *
from .filters import HardwareFilter, PrintersFilter
from .forms import HardwareForm
from django.core.paginator import Paginator
from django.db.models import Q
from .BGInfo import *
from .SETTING import *



def index(request):
    search_query = request.GET.get('search', '')
    BGInfo_query = request.GET.get('BGInfo')
    update_query = request.GET.get('update')

    Toner = Printer_Color.objects.all()

    if search_query:
        hardware = Hardware.objects.filter(Q(serial_number__endswith = search_query) 
                                         | Q(employ__surname__icontains = search_query)
                                         | Q(buildings__building__startswith = search_query))
    else:
        hardware = Hardware.objects.all().select_related('type_dev').select_related('employ').select_related('buildings')

    if BGInfo_query:
        user = request.GET.get('BGInfo')
        CONN = connection_pyodbc()
        CONN_DB = connection(BD)
        BGInfo = query_info_user(user, CONN)
        BGUsers = take_users_from_db(CONN_DB)
        context = {
            'BGUsers': BGUsers,
            'BGInfo': BGInfo,
            'Toner': Toner,
            }
        return render(request, 'dev/main.html', context)
      
    elif update_query:
        CONN = connection_pyodbc()
        CONN_DB = connection(BD)
        users = take_users_from_db_BGInfo(CONN) 
        insert_users_to_db(CONN_DB, users)

        return redirect('index')

    CONN_DB = connection(BD)   
    BGUsers = take_users_from_db(CONN_DB)
    context = {
        'BGUsers': BGUsers,
        'Toner': Toner,
        } 

    
    return render(request, 'dev/main.html', context)




def printers(request):
    f = PrintersFilter(request.GET, queryset = Printers.objects.order_by('name_printers'))

    #printers = Printers.objects.order_by('name_printers')
    context = {
        'filters': f
    }
    return render(request, 'dev/printers.html', context) 

def hardware(request):
    search_query = request.GET.get('search', '')

    if search_query:
        hardware = Hardware.objects.filter(Q(serial_number__endswith = search_query) | Q(employ__surname__icontains = search_query))
    else:
        hardware = Hardware.objects.all().select_related('type_dev').select_related('employ').select_related('buildings')     

    paginator = Paginator(hardware, 50)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    
    if page.has_previous():
        page_prev = f'?page={page.previous_page_number()}'
    else:
        page_prev = ''

    if page.has_next():
        page_next = f'?page={page.next_page_number()}'
    else:
        page_next = ''


    context = {'page': page, 'page_prev':page_prev, 'page_next': page_next}
    return render(request, 'dev/hardware.html', context)


def createHardware(request):
    form = HardwareForm()
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            form = HardwareForm
            context = {'form':form,'accept':True}
            return render(request, 'dev/createHardware.html', context)
        else:
            errors = form.errors
            context = {'form':form, 'errors': errors}
            return render(request, 'dev/createHardware.html', context) 
    
    context = {'form':form}

    return render(request, 'dev/createHardware.html', context)

def update (request, hardware_id):
    change = Hardware.objects.get(id = hardware_id)
    form = HardwareForm(instance = change)
    if request.method == 'POST':
        form = HardwareForm(request.POST, instance = change)
        if form.is_valid():
            form.save()
            return redirect ('hardware')
        else:
            errors = form.errors
            change = Hardware.objects.get(id = hardware_id)
            print(errors)
            form = HardwareForm(instance = change)
            context = {'update':form, 'errors': errors}
            return render(request, 'dev/hardware.html', context) 

    context = {'update':form}
    return render(request, 'dev/hardware.html', context)    

def delete(request, hardware_id):
    hardware = Hardware.objects.get(id = hardware_id)
    if request.method == 'POST':
        hardware.delete()
        return redirect ('hardware')
    context = {'delete':hardware}
    return render(request, 'dev/hardware.html', context)





