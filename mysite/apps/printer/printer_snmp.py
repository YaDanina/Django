# import sys, os
# from django.conf import settings
# settings.configure()
# sys.path.insert(0, os.path.join(r'E:\Django\mysite\mysite\mysite\apps'))
# from printer.models import *
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import sys 
sys.path.insert(0,r'E:\Django\mysite\mysite')
from concurrent.futures import ProcessPoolExecutor, as_completed
from pysnmp.hlapi import *
import sqlite3
from common_functions import *
from OID import *
from datetime import datetime
import re
from tabulate import tabulate


def take_data_from_db(db, color = False):
    buffer = []
    printers = []
    connection = create_connection(db)
    if color:
        query = 'select * from dev_printers where name_printers like "Xerox%"'
        with connection as con:
            result = con.execute(query)
            for row in result:
                printers.append(list(row))   
        
        for row in printers:
            match = re.search(r'Xerox_(7(1|4|5|8)\w+)_', row[1])
            if match:
                buffer.append(row)
        return buffer        
    else:
        query = 'select * from dev_printers'
        with connection as con:
            result = con.execute(query)
            for row in result:
                printers.append(list(row))
        return printers

        #alive = check_reachable(printers, ping=True)
        # result = check_reachable(alive, snmp = True, color=True)

def insert_data_to_db(db, color = False):
    connection = create_connection(db)
    if color:
        query = 'insert or replace into printer_printer_color values (?,?,?,?,?,?,?)'
        db_data = []
        today = str(datetime.now().replace(microsecond=0))
        alive_printers = multiprocces_executor(take_data_from_db(db, color=True), ping=True)
        snmp_data = multiprocces_executor(alive_printers, snmp=True, color=True)
        ids = 0
        for row in snmp_data:
            ids += 1
            date = today
            name_printers = row[1]
            toner_black = int((int(row[7]) * 100)/int(row[6]))
            toner_cyan = int((int(row[9]) * 100)/int(row[8]))
            toner_magenta = int((int(row[11]) * 100)/int(row[10]))
            toner_yellow = int((int(row[13]) * 100)/int(row[12]))
            buffer = [ids, date, name_printers, toner_black, toner_cyan, toner_magenta, toner_yellow]
            db_data.append(tuple(buffer))
        with connection as con:
            con.executemany(query, db_data)
    # else:
    #     query = 'insert or replace into printer_printers_stat values (?,?,?,?,?,?,?)'


              


        
        

    



def make_data_for_site(data):
    result = {}
    for row in data:
        result[row[1]] = {'Black':f'{int((int(row[7]) * 100)/int(row[6]))}%',
                          'Cyan': f'{int((int(row[9]) * 100)/int(row[8]))}%',
                          'Magenta': f'{int((int(row[11]) * 100)/int(row[10]))}%',
                          'Yellow' : f'{int((int(row[13]) * 100)/int(row[12]))}%'
                          }
    print(result)    





if __name__ == '__main__':
    result = insert_data_to_db('db.sqlite3', color=True)
    
    
    
    
