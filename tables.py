from prettytable import PrettyTable
from math import log10, sqrt, log


class Tables():
    def __init__(self, data):
        self.list_of_func_x_table_5 = None
        self.list_table_1 = None
        self.list_sorted_table_2 = None
        self.dict_table_3 = None
        self.dict_table_4 = None
        self.dict_table_6 = None
        self.data = data

    def selecting_and_printing_table(self, number_of_table, size_of_interval=0, count_of_steps=0):
        if number_of_table == 1:
            return self.first_table()
        elif number_of_table == 2:
            return self.second_table()
        elif number_of_table == 3:
            return self.third_table()
        elif number_of_table == 4:
            return self.forth_table(size_of_interval, count_of_steps)
        elif number_of_table == 5:
            return self.fifth_table()
        elif number_of_table == 6:
            return self.sixth_table(size_of_interval)

    def first_table(self):
        self.list_table_1 = []
        table = PrettyTable()
        table.field_names = ["i", 'X']
        for i in range(0, len(self.data)):
            table.add_row([i + 1, self.data[i]])
            self.list_table_1.append(self.data[i])
        print("Т а б л и ц а 1. Выборочные данные X")
        print(table)

    def second_table(self):
        self.list_sorted_table_2 = []
        table = PrettyTable()
        table.field_names = ["i", 'X']
        sorted_data = sorted(self.data)
        for i in range(0, len(sorted_data)):
            table.add_row([i + 1, sorted_data[i]])
            self.list_sorted_table_2.append(sorted_data[i])
        print("Т а б л и ц а 2. Ранжированный ряд случайной величины Х")
        print(table)

    def third_table(self):
        list_number = []
        list_elem = []
        list_ni = []
        list_pi = []
        table = PrettyTable()
        table.field_names = ["i", 'Xi', 'ni', 'pi']

        dict = {}
        count_of_number = 1
        sorted_data = self.list_sorted_table_2

        for i in range(0, len(sorted_data) - 1):
            if sorted_data[i] == sorted_data[i + 1]:
                count_of_number += 1
                dict[sorted_data[i]] = count_of_number

            elif sorted_data[i] != sorted_data[i + 1] and sorted_data[i] in dict:
                dict[sorted_data[i]] = count_of_number
                count_of_number = 1

            else:
                count_of_number = 1
                dict[sorted_data[i]] = count_of_number

        number_of_element = 1
        for key, value in dict.items():
            table.add_row([number_of_element, key, value, f'{value}/{len(self.data)}'])
            list_number.append(number_of_element)
            list_elem.append(key)
            list_ni.append(value)
            list_pi.append(value / len(self.data))
            number_of_element += 1
        self.dict_table_3 = {
            "i": list_number,
            "Xi": list_elem,
            "ni": list_ni,
            "pi": list_pi
        }
        last_element = self.list_sorted_table_2[-1]
        if (last_element not in self.dict_table_3["Xi"]):
            table.add_row([number_of_element, last_element, 1, f'{1}/{len(self.data)}'])
            list_number.append(number_of_element)
            list_elem.append(last_element)
            list_ni.append(1)
            list_pi.append(1 / len(self.data))

        print("Т а б л и ц а 3. Дискретный вариационный ряд")
        print(table)

    def forth_table(self, size_of_interval, count_of_steps):
        number_elements = []
        interval = []
        ni = []
        pi = []
        table = PrettyTable()
        table.field_names = ["i", 'Xi < X < Xi+1', 'ni', 'pi']
        unique_data_values = self.list_sorted_table_2
        len_of_data = len(self.list_sorted_table_2)
        min_value = unique_data_values[0]
        current_value = min_value
        number_of_element = 1
        count_of_element = 0  # Равно одному потому что изначально уже добавляю первый элемент из списка
        for_a_crutch = unique_data_values[0]
        last_index_of_element = 0
        for step in range(count_of_steps):
            prev_value = current_value
            current_value += size_of_interval
            for i in range(last_index_of_element, len(unique_data_values)):
                if unique_data_values[i] == for_a_crutch:  # костыль чтобы у меня не удалялись лишние элементы доделать если пойму как можно сделать иначе
                    count_of_element += 1
                elif prev_value < unique_data_values[i] <= current_value:
                    count_of_element += 1
                else:
                    last_index_of_element += count_of_element
                    table.add_row([number_of_element, f'{prev_value} - {current_value}', count_of_element,
                                   f'{count_of_element}/{len_of_data}'])
                    number_elements.append(number_of_element)
                    interval.append([prev_value, current_value])
                    ni.append(count_of_element)
                    pi.append(count_of_element / len_of_data)
                    count_of_element = 0

                    break
            else:
                if number_of_element == count_of_steps:
                    table.add_row([number_of_element, f'{prev_value} - {current_value}', count_of_element,
                                   f'{count_of_element}/{len(unique_data_values)}'])
                    number_elements.append(number_of_element)
                    interval.append([prev_value, current_value])
                    ni.append(count_of_element)
                    pi.append(count_of_element / len_of_data)

            number_of_element += 1
        self.dict_table_4 = {
            "i": number_elements,
            "interval": interval,
            "ni": ni,
            "pi": pi
        }
        print(table)

    def fifth_table(self):
        table = PrettyTable()
        table.field_names = ["i", 'F(x)']
        ni_of_current_interval = self.dict_table_4["ni"]
        func_x = 0
        self.list_of_func_x_table_5 = []
        for i in range(len(ni_of_current_interval)):
            prev_func_x = func_x
            func_x += ni_of_current_interval[i]
            func_x_calculation = func_x / len(self.data)
            if(i == 0):
                table.add_row([i + 1, f'{func_x}/{len(self.data)}'])
            else:
                table.add_row([i+1, f"{prev_func_x}/{len(self.data)} + {ni_of_current_interval[i]}/{len(self.data)} = {func_x}/{len(self.data)}"])
            self.list_of_func_x_table_5.append(func_x_calculation)

        print(table)



    def sixth_table(self, size_of_interval):
        table = PrettyTable()
        table.field_names = ["i", 'Xi', 'pi*', 'ni/h*N']
        list_of_intervals = self.dict_table_4["interval"]
        ni_of_current_interval = self.dict_table_4["ni"]
        pi_of_current_interval = self.dict_table_4["pi"]

        list_mid_value_interval = []
        list_pi_of_interval = pi_of_current_interval.copy()
        list_probability_density = []

        for i in range(len(list_of_intervals)):
            mid_value_of_interval = (list_of_intervals[i][0] + list_of_intervals[i][1]) / 2
            pi = pi_of_current_interval[i]
            probability_density = ni_of_current_interval[i] / (size_of_interval * len(self.data))

            table.add_row([i + 1, mid_value_of_interval, pi, probability_density])
            list_mid_value_interval.append(mid_value_of_interval)
            list_probability_density.append(probability_density)

        self.dict_table_6 = {
            'Xi': list_mid_value_interval,
            'pi*': list_pi_of_interval,
            'density': list_probability_density
        }

        print(table)

    def selecting_and_geting_value_of_table(self, number_of_table):
        if number_of_table == 1:
            return self.list_table_1
        elif number_of_table == 2:
            return self.list_sorted_table_2
        elif number_of_table == 3:
            return self.dict_table_3
        elif number_of_table == 4:
            return self.dict_table_4
        elif number_of_table == 5:
            return self.list_of_func_x_table_5
        elif number_of_table == 6:
            return self.dict_table_6
