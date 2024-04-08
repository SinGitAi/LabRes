from prettytable import PrettyTable
from math import log10, sqrt, log

class Tables():
    def __init__(self, data):
        self.data = data


    def selecting_and_printing_table(self, number_of_table):
        if number_of_table == 1:
            return self.first_table()
        elif number_of_table == 2:
            return self.second_table()
        elif number_of_table == 3:
            return self.third_table()

    def first_table(self):
        self.dict_table_1 = {}
        table = PrettyTable()
        table.field_names = ['№', 'X']
        for i in range(0, len(self.data)):
            table.add_row([i + 1, self.data[i]])
            self.dict_table_1[i + 1] = self.data[i]
        print("Т а б л и ц а 1. Выборочные данные X")
        print(table)

    def second_table(self):
        self.dict_table_2 = {}
        table = PrettyTable()
        table.field_names = ['№', 'X']
        sorted_data = sorted(self.data)
        for i in range(0, len(sorted_data)):
            table.add_row([i+1, sorted_data[i]])
            self.dict_table_2[i + 1] = sorted_data[i]
        print("Т а б л и ц а 2. Ранжированный ряд случайной величины Х")
        print(table)

    def third_table(self):
        list_number = []
        list_elem = []
        list_ni = []
        list_pi = []
        count_of_number = 0
        table = PrettyTable()
        table.field_names = ['№', 'Xi', 'ni', 'pi']
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if self.data[i] == self.data[j]:
                    count_of_number += 1
            # TODO
            table.add_row([i + 1, self.data[i], count_of_number, f'{count_of_number}/{len(self.data)}'])
            list_number.append(i + 1)
            list_elem.append(self.data[i])
            list_ni.append(count_of_number)
            list_pi.append(f'{count_of_number}/{len(self.data)}')
            count_of_number = 0

        self.dict_table_3 = {
            "i": list_number,
            "Xi": list_elem,
            "ni": list_ni,
            "pi": list_pi
        }
        print("Т а б л и ц а 3. Дискретный вариационный ряд")
        print(table)


    def selecting_and_geting_value_of_table(self, number_of_table):
        if number_of_table == 1:
            return self.dict_table_1
        elif number_of_table == 2:
            return self.dict_table_2
        elif number_of_table == 3:
            return self.dict_table_3



