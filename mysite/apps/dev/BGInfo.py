import os
import pyodbc
import sqlite3
import datetime
from datetime import timedelta

def connection(db):
    conn = sqlite3.connect(db)
    return conn


def connection_pyodbc():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=agBGInfo.rskh.local;DATABASE=BGInfo')
    return conn


def take_users_from_db_BGInfo(connection):
    buffer = []
    query = 'select * from dbo.BGInfoTable'
    date = datetime.datetime.now() - datetime.timedelta(days=7)
    with connection as con:
        result = con.execute(query)
        for row in result:
            if row[0] > date and row[1] not in buffer:
                buffer.append(row[1])
    return buffer

def insert_users_to_db(connection, users):
    with connection as con:
        con.execute("delete from BGInfo_users where user like '_%'")
        for i in users:
            con.execute(f'insert into BGInfo_users values ("{i}")')




def take_users_from_db(connection):
    buffer = []
    query = 'select * from BGInfo_users'
    with connection as con:
        result = con.execute(query)
        buffer = [row[0] for row in result]

    return buffer    




def query_info_user(user, conn):
    buffer = []
    date = datetime.datetime.now() - datetime.timedelta(days=30)
    query = f"select * from dbo.BGInfoTable where User_Name = '{user}' order by Time_Stamp DESC"
    with conn as f:
        result = f.execute(query)
        for row in result:
            if row[0] > date:
                new_dict = {}
                new_dict['Date'] = str(row[0])
                new_dict['Host'] = row[2]
                new_dict['User'] = row[1]
                new_dict['IP_Address'] = row[10]
                buffer.append(new_dict)

    return buffer  




if __name__ == "__main__":
    db = os.path.join('e:/Django/mysite/mysite/db.sqlite3')
    conn_db = connection(db)
    conn = connection_pyodbc()
    users = take_users_from_db_BGInfo(conn) 
    insert_users_to_db(conn_db, users)
 
    

