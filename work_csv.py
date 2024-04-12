import csv
csvi = []

def read_table_laplas():
    # Открываем CSV файл для чтения с указанием кодировки без BOM
    with open('data/Zi.csv', newline='', encoding='utf-8-sig') as csvfile:
        # Создаем объект чтения с указанием разделителя
        csvreader = csv.reader(csvfile, delimiter=';')
        dict ={}
        # Читаем данные построчно
        for row in csvreader:
            row = [float(value.replace(',', '.')) for value in row]
            dict[row[0]] = row[1]

    return dict
