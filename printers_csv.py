import csv
import os
import sqlite3
import re

def create_list_from_csv(file_csv):
    '''
    Возвращает список из CSV файла выгруженного с принт-сервера
    '''
    result = []
    with open(file_csv) as f:
        file = csv.reader(f)
        for row in file:
            result.append(row)
    result = [i for i in result if i[0].startswith('1')]  

    return result

def sort_by_type(file_csv):
    '''
    Возвращает список списков (Плоттеры, МФУ, Принтеры, Принтеры ППС) из списка принтеров выгруженного с принт-сервера.
    '''
    printers = create_list_from_csv(file_csv)
    PLOTTERS = []
    MFU = []
    PPS = []
    PRINTERS = []
    regex_plotter = re.compile(r'HP_(5|T)\S+')
    regex_MFU = re.compile(r'Xerox_(5|7)\S+')
    regex_PPS  = re.compile(r'(PPS|pps)_\S+')

    for i, row in enumerate(printers):
        match_plotter = regex_plotter.search(row[1])
        match_MFU = regex_MFU.search(row[1])
        match_PPS = regex_PPS.search(row[1])
        if match_plotter:
            PLOTTERS.append(i)
        elif match_MFU:
            MFU.append(i)
        elif match_PPS:
            PPS.append(i)        
    

    for i, row in enumerate(printers):
        if i in PLOTTERS:
            row.insert(2, 'ПЛОТТЕР')
        elif i in MFU:
            row.insert(2, 'МФУ')
        elif i in PPS:
            row.insert(2, 'ППС')
        else:
            row.insert(2, 'ПРИНТЕР')

    printers = sorted_printers(printers)
    
    for i, row in enumerate(printers, 1):
        row.insert(0,i)

    return printers    


def sorted_printers(printers):
    printers = [sorted(row, key=len, reverse=True) for row in printers]
    for row in printers:
        if row[0] == '' or row[1] == '' or row[2] == '':
            printers.remove(row)        
    return printers


def create_connection(database):
    '''
    Возвращает соединение с базой данных
    '''
    conn = sqlite3.connect(database)
    return conn

def select_data_from_db(connection):
    '''
    Возвращает список из уже существующих принтеров в базе данных.
    '''
    result = []
    query = 'select * from dev_printers'
    for row in connection.execute(query):
        result.append(list(row))

    return result

def change_data_db(connection, data, change_count = False, change = False, diff = None):
    if change:
        query = 'replace into dev_printers values(?,?,?,?)'
        with connection as conn:
            conn.execute(query, tuple(data))
    if change_count:
        buffer = []
        query_delete = "delete from dev_printers where name_printers like '_%'"
        query = 'insert or replace into dev_printers values(?,?,?,?)'
        for row in data:
            buffer.append(tuple(row))        
        with connection as conn:
            conn.execute(query_delete)
            conn.executemany(query, buffer)      

def compare_db(connection, new_data, db_data):
    '''
    Сравнивает принтеры из базы данных и принтеры из принт-сервера.
    Если длина списков равна, сравнивает списки построчно, если строка не равна, обращаемся к функции change_data_db и меняем запись в базе данных.
    Если длина не равна, добавляем или удалаяем запись в базе данных
    ''' 
    data = []
    buffer = []
    if len(new_data) == len(db_data):
        for i,row in enumerate(new_data):
            if row == db_data[i]:
                continue
            else:
                change_data_db(connection, row, change = True)
    elif len(new_data) != len(db_data):
        if len(new_data) < len(db_data):
            diff = len(db_data) - len(new_data) 
            change_data_db(connection, new_data, change_count = True, diff = diff)
        else:
            change_data_db(connection, new_data, change_count = True)

    


if __name__ == '__main__':
    conn = create_connection('db.sqlite3')
    new_data = sort_by_type('port.csv')
    db_data = select_data_from_db(conn)
    compare_db(conn, new_data, db_data)

   
    



