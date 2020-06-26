from .BGInfo import *
import os


'''База данных SQLITE основная'''
BD = os.path.join('e:/Django/mysite/mysite/db.sqlite3')
'''Подключение к базе данных BGInfo'''
CONN = connection_pyodbc()
'''Подключение к базе данных SQLITE'''
CONN_DB = connection(BD)
