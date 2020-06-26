import csv
import re
from tabulate import tabulate
import pandas

header = ['Дата создания', 'Дата_последнего_входа', 'Пользователь', 'Почтовый_ящик']
Azimut_Freestyle = []
Azimut_Freestyle.append(header)
Azimut_Valset = []
Azimut_Valset.append(header)
Mercure_Accor = []
Mercure_Accor.append(header)
Park_Inn = []
Park_Inn.append(header)
Radisson = []
Radisson.append(header)
RidersLodge = []
RidersLodge.append(header)
Rosa_Hall = []
Rosa_Hall.append(header)
Rosa_Village = []
Rosa_Village.append(header)
Tulip_Golden = []
Tulip_Golden.append(header)
Tulip_Inn = []
Tulip_Inn.append(header)
Varezhka = []
Varezhka.append(header)
Vysota = []
Vysota.append(header)


regex = re.compile(r'OU=((\w+|Vysota&Berloga)),')

with open('test.csv', encoding='utf-8') as f:
    name = []
    buffer = []
    text = csv.reader(f)
    for row in text:
        buffer.append(row)
        match = regex.search(row[0])
        if match:
            if match.group(1) not in name:
                name.append(match.group(1))

def write_to_csv(data, name):
    with open(f'{name}.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row in data:
            write.writerow(row)

def conver_to_excel(name):
    read_file = pandas.read_csv(f'{name}.csv')
    read_file.to_excel(f'{name}.xlsx', index = None, header = True)            

# def to_text(data, name):
#     with open(f'{name}.txt', 'w', encoding='utf-8') as f:
#         f.write(tabulate(data))


for row in sorted(buffer):
    match = regex.search(row[0])
    if match:
        name = match.group(1)
        if name == 'Azimut_Freestyle':
            if row not in Azimut_Freestyle:
                Azimut_Freestyle.append(row[1:5])
                write_to_csv(Azimut_Freestyle, name)
                conver_to_excel(name)




