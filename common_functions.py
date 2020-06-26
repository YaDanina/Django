from concurrent.futures import ProcessPoolExecutor, as_completed
import sqlite3
import csv
import os, glob
from tabulate import tabulate
from pprint import pprint
import re
import subprocess
from datetime import datetime
from pysnmp.hlapi import *
from OID import *


today = str(datetime.now()).split()[0]

def create_list_from_csv(file_csv):
    result = []
    with open(file_csv) as f:
        file = csv.reader(f, delimiter=';')
        head = next(file)
        for row in file:
            result.append(row)
    return result


def create_connection(database):
    conn = sqlite3.connect(database)
    return conn

def change_format(date):
    regex = re.compile(r'(?P<day>\d+)\.(?P<month>\d+)\.(?P<year>\d+) +(?P<time>\S+)')
    match = regex.search(date)
    if match:
        day = match.group('day')
        month = match.group('month')
        year = match.group('year')
        time = match.group('time')
        if len(day) == 1:
            day = '0' + day
        else:
            pass
        if len(month) == 1:
            month = '0' + month
        else:
            pass
        result = f'{year}-{month}-{day}'
        return result


def change_or_fill_empty_date(date):
    '''
    Если дата пустая то, возвращаем стандартную дату:
    '''
    if date[0] == '':
        new_date = '2007-01-01'
        date.pop(0)
        date.insert(0, new_date)
        return date   
    else:
        new_date = change_format(date[0])
        date.pop(0)
        date.insert(0, new_date)
        return date     


def send_ping(data, ping = False):
    check = subprocess.run(f'ping {data[2]} -n 2',
                                shell=True,
                                stdout=subprocess.PIPE)
    if check.returncode == 0:
        return data

def get_snmp(ip, OID):
    _, _, _, printer = next(getCmd(SnmpEngine(),
                            CommunityData('public'),
                            UdpTransportTarget((ip, 161)),
                            ContextData(),
                            ObjectType(ObjectIdentity(OID))
                            ))
    for name, i in printer:
        result = i
    return result


def data_for_db(data, color = False):
    snmp_data = []
    if color:
        date = today
        name_printers = data[1]
        ip = data[2]
        type_printers = data[3]
        serial_number = get_snmp(ip, X_Serial_Number)
        page_count = get_snmp(ip, X_Page_Count)
        capacity_toner_black = get_snmp(ip, X_Black_Capacity)
        toner_count_black = get_snmp(ip, X_Black_Current)
        capacity_toner_cyan = get_snmp(ip, X_Cyan_Capacity)
        toner_count_cyan = get_snmp(ip, X_Cyan_Current)
        capacity_toner_magenta = get_snmp(ip, X_Magenta_Capacity)
        toner_count_magenta = get_snmp(ip, X_Magenta_Current)
        capacity_toner_yellow = get_snmp(ip, X_Yellow_Capacity)
        toner_count_yellow = get_snmp(ip, X_Yellow_Current)
        # cartridge_type = get_snmp(ip, K_Cartridge)
        buffer = [date, name_printers, 
                    ip, type_printers, 
                    serial_number, 
                    page_count, 
                    capacity_toner_black, 
                    toner_count_black, 
                    capacity_toner_cyan, 
                    toner_count_cyan,
                    capacity_toner_magenta,
                    toner_count_magenta,
                    capacity_toner_yellow,
                    toner_count_yellow]
        return buffer        
    else:
        for row in data:
            date = today
            name_printers = row[1]
            ip = row[2]
            type_printers = row[3]
            serial_number = get_snmp(ip, K_Serial_Number)
            page_count = get_snmp(ip, K_Page_Count)
            capacity_toner_black = get_snmp(ip, K_Black_Capacity)
            toner_count_black = get_snmp(ip, K_Black_Current)
            cartridge_type = get_snmp(ip, K_Cartridge)
            buffer = [date, name_printers, ip, type_printers, serial_number, page_count, capacity_toner_black, toner_count_black, cartridge_type]
            snmp_data.append(buffer)
        return snmp_data    

def multiprocces_executor(printers, ping = False, snmp = False, color = False):
    if ping:
        alive = []
        with ProcessPoolExecutor(max_workers=10) as executor:
            future = [
                executor.submit(send_ping, printer) for printer in printers
            ] 
        for f in as_completed(future):
            result = f.result()
            if result:
                alive.append(result)
        return alive
    elif snmp:
        snmp_list = []
        with ProcessPoolExecutor(max_workers=10) as executor:
            future = [
                executor.submit(data_for_db, printer, color = color) for printer in printers
            ]
        for f in as_completed(future):
            result = f.result()
            if result:
                snmp_list.append(result)
        return snmp_list       











if __name__ == '__main__':
    buffer = []
    query = 'select * from dev_printers where name_printers like "Kyocera%"'
    conn = create_connection('db.sqlite3')
    with conn as c:
        file = c.execute(query)
        for i in file:
            buffer.append(list(i))
    result = check_reachable(buffer)
    
    

    
           



'''
Схема, поля вставки данных Hardware


for i in hard:
    hardware = Hardware(id = i[2], date = i[0], type_dev_id = i[3], organization = i[4], vendor = i[5], model = i[6], serial_number = i[7], inv_number = i[8], status = i[9], buildings_id = i[10], room = i[11], employ_id = i[12], note = i[15], date_of_sale = i[16], seller = i[18], MOL = i[24])
    hardware.save()

'''

    # schema_building = '''CREATE TABLE '''
    # result = []
    # for file in glob.glob('*.csv'):
    #     if file == 'building.csv':
    #         data_building = create_list_from_csv(file)
    #         result.append(data_building)
    #         #print(data_building)
    #     elif file == 'employ.csv':
    #         data_employ = create_list_from_csv(file)
    #         result.append(data_employ)
    #         #print(data_employ)
    #     elif file == 'hardware.csv':
    #         data_hardware = create_list_from_csv(file)
    #         result.append(data_hardware)
    #         print(data_hardware[:3])
    #         #for i in data_hardware:
    #             #print(i[4])
    #     elif file == 'type_dev.csv':
    #         data_type_dev = create_list_from_csv(file)
    #         result.append(data_type_dev) 