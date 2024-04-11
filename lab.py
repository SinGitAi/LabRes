from prettytable import PrettyTable
from math import log10, sqrt, log
# Лаба расчитана на значения в диапозоне от 1 до 9999 и без плавующей точки
# DATA = [51, 89 ,51 ,18, 51 ,81 ,30 ,39, 4 ,31 ,51, 26, 39, 51 ,78 ,74 ,11 ,48 ,16 ,76 ,57 ,32 ,99 ,69 ,94 ,40 ,53 ,46 ,73 ,14 ,78 ,16 ,60 ,94 ,12 ,60 ,48 ,15, 86 ,17 ,27 ,15 ,28 ,31 ,36 ,99 ,33 ,17 ,42,14]
DATA = [1782, 1963, 1791, 1287, 1063, 1222, 1206, 1329, 1528, 1238, 1848, 1858, 1289, 1586, 772,
        1266, 1242, 1816, 951, 1693, 1643, 1497, 1280, 1760, 1717, 1212, 1238, 1259, 1901, 1022,
        818, 1894, 1972, 1216, 1973, 1595, 1324, 1206, 1136, 1111, 1670, 1765, 1517, 762, 2092,
        1279, 1942, 437, 408, 995, 2101, 2132, 1100, 1235, 1036, 1264, 1275, 1386, 1652, 1760, 1308,
        812, 1514, 1197, 1222, 1907, 1172, 1137, 1709, 1150, 1456, 1519, 1843, 1085, 1525, 1668, 981,
        1662, 1216, 1808, 146, 1098, 1917, 1492, 1510]
SORTED_DATA_UNIQUE = [146, 408, 437, 762, 772, 812, 818, 951, 981, 995, 1022, 1036, 1063, 1085, 1098, 1100, 1111,
               1136, 1137, 1150, 1172, 1197, 1206, 1212, 1216, 1222, 1235, 1238, 1242, 1259, 1264, 1266, 1275,
               1279, 1280, 1287, 1289, 1308, 1324, 1329, 1386, 1456, 1492, 1497, 1510, 1514, 1517, 1519, 1525,
               1528, 1586, 1595, 1643, 1652, 1662, 1668, 1670, 1693, 1709, 1717, 1760, 1765, 1782, 1791, 1808,
               1816, 1843, 1848, 1858, 1894, 1901, 1907, 1917, 1942, 1963, 1972, 1973, 2092, 2101, 2132]
SORTED_DATA = [146, 408, 437, 762, 772, 812, 818, 951, 981, 995, 1022, 1036, 1063, 1085, 1098, 1100, 1111, 1136,
               1137, 1150, 1172, 1197, 1206, 1206, 1212, 1216, 1216, 1222, 1222, 1235, 1238, 1238, 1242, 1259, 1264,
               1266, 1275, 1279, 1280, 1287, 1289, 1308, 1324, 1329, 1386, 1456, 1492, 1497, 1510, 1514, 1517, 1519,
               1525, 1528, 1586, 1595, 1643, 1652, 1662, 1668, 1670, 1693, 1709, 1717, 1760, 1760, 1765, 1782, 1791,
               1808, 1816, 1843, 1848, 1858, 1894, 1901, 1907, 1917, 1942, 1963, 1972, 1973, 2092, 2101, 2132]
# DATA = [27, 27, 29, 29, 29, 31, 31, 31, 33, 33, 34, 34, 34, 34, 35, 35, 35, 35, 35, 36, 36, 36,
#          36, 36, 37, 37, 37, 37, 37, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 41, 41, 41,
#          41, 41, 41, 42, 43, 43, 43, 44, 44, 44, 44, 45, 45, 46, 47, 47, 48, 49, 49, 50, 50, 51,
#          52, 52, 54, 54, 55, 57, 58, 59, 69, 77, 89, 89, 90, 90, 95, 99, 108, 116, 123]
# DATA = [148, 155, 156, 156, 157, 157, 158, 159, 159, 159, 160, 160, 160, 161, 161, 161, 161, 161,
#          161, 162, 162, 162, 162, 162, 162, 163, 163, 163, 163, 163, 163, 163, 163, 163, 164, 164,
#          164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 165, 165, 165, 165,
#          165, 165, 165, 165, 165, 165, 165, 165, 165, 165, 165, 166, 166, 166, 166, 166, 166, 166,
#          166, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 167, 168, 168, 168,
#          168, 168, 168, 168, 168, 168, 168, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169,
#          169, 169, 169, 169, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170,
#          170, 171, 171, 171, 171, 171, 171, 171, 171, 171, 171, 171, 172, 172, 172, 172, 172, 172,
#          172, 172, 172, 172, 172, 172, 173, 173, 173, 173, 173, 173, 173, 173, 173, 174, 174, 174,
#          174, 174, 174, 175, 175, 175, 175, 175, 175, 176, 176, 176, 176, 176, 176, 176, 176, 176,
#          176, 177, 178, 178, 178, 178, 179, 179, 179, 180, 180, 180, 181, 181, 182, 183, 184, 185,
#          186, 187, 190]
# def first_table(data):

    # mas = list(map(int, input().split()))
    # mas = [51, 89 ,51 ,18, 51 ,81 ,30 ,39, 4 ,31 ,51, 26, 39, 51 ,78 ,74 ,11 ,48 ,16 ,76 ,57 ,32 ,99 ,69 ,94 ,40 ,53 ,46 ,73 ,14 ,78 ,16 ,60 ,94 ,12 ,60 ,48 ,15, 86 ,17 ,27 ,15 ,28 ,31 ,36 ,99 ,33 ,17 ,42,14]
    # table = PrettyTable()
    # table.field_names = ['№', 'X']
    # print(DATA)
    # 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306
    # for i in range(0, len(data) - 1):
    #     table.add_row([i+1, data[i]])
    #
    # print("Выборочные данные X")
    # print(table)
    
# def second_table(data):
#     table = PrettyTable()
#     table.field_names = ['№', 'X']
#     sortedData = sorted(data)
#     for i in range(0, len(sortedData) - 1):
#         table.add_row([i+1, sortedData[i]])
    # print("Ранжированный ряд для велечины X\n(по увелечению X)")
    # print(table)
    # return sortedData

# def find_divisors(n):
#     i = 2
#     divisors = []
#
#     while i ** 2 <= n:
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i :
#                 divisors.append(n // i)
#         i += 1
#     divisors.sort()
    # sorted_divisors = []
    # for i in range(0, len(divisors)):
    #     j = len(str(divisors[i]))
    #     k = len(str(n//100))
    #     if(not j < k):
    #         sorted_divisors.append(divisors[i])
    # return divisors

# def third_table(data):
#     list_poryad_nomer = []
#     list_elem = []
#     list_ni = []
#     list_pi = []
#     countOfNumber = 0
#     data_without_repeat = set()
#     table = PrettyTable()
#     table.field_names = ['№', 'Xi', 'ni', 'pi']
#     for i in range(0, len(data)-1):
#         for j in range(0, len(data)-1):
#             if(data[i] == data[j]):
#                 countOfNumber+=1
#                 data_without_repeat.add(i)
#
#         table.add_row([i+1, data_without_repeat[i], countOfNumber, f'{countOfNumber}/{len(data)}'])
#         list_poryad_nomer.append(i+1)
#         list_elem.append(data[i])
#         list_ni.append(countOfNumber)
#         list_pi.append(f'{countOfNumber}/{len(data)}')
#         countOfNumber = 0
#     dictForSchet = {
#         "i": list_poryad_nomer,
#         "Xi": list_elem,
#         "ni": list_ni,
#         "pi": list_pi
#     }
#     return table,
        
   
# def interval_calculation(*, min_value, max_value, count_elements):
#     scope_of_interval = max_value - min_value
#     size_of_ineterval = int(scope_of_interval / (1 + 3.28 * log(count_elements)))
#     print(interval_step_check(size_of_ineterval, second_table(DATA), scope_of_interval))
    # print(scope_of_ineterval, size_of_ineterval)
    

# def check_step(size_of_ineterval, elements):
#     min_element = min(elements)
#     current_value = min_element
#     count_of_steps = 0
#     max_element = max(elements)
#     while(current_value < max_element):
#         current_value += size_of_ineterval
#         count_of_steps+=1
#         if(count_of_steps > 15):
#             return False
#     return current_value == max_element #Если шаг равен то возвращает true
    
# def interval_step_check(size_of_ineterval, elements, scope_of_ineterval):
#     correct_size_interval = size_of_ineterval
#     if(check_step(correct_size_interval+1, elements)):
#         return correct_size_interval+1
#     if (check_step(correct_size_interval - 1, elements)):
#         return correct_size_interval - 1
#     if(not check_step(correct_size_interval, elements)):
#         divisors = find_divisors(scope_of_ineterval)
#         for i in divisors:
#             correct_size_interval = i
#             if (check_step(correct_size_interval, elements)):
#                 break
#
#     return correct_size_interval


# def filter_divisors(divisors, size_of_interval):
#     len_size_interval = len(str(size_of_interval))
#     margin_of_error = 0
#     if((len_size_interval >= 3) or (len_size_interval == 3 and 500<size_of_interval<1000)):
#         margin_of_error = 100
#     elif(len_size_interval == 3):
#         margin_of_error = 10
#     else:
#         margin_of_error =
# interval_calculation(min_value=min(DATA), max_value=max(DATA), count_elements=len(DATA))



# НЕЛЬЗЯ УДАЛЯТЬ СУКА
# dict = {}
# count = 1
# # 148, 155, 156, 156, 157, 157,  157 158, 159, 159, 159,
# for i in range(0, len(DATA)-1):
#     if(DATA[i] == DATA[i+1]):
#         count += 1
#         dict[DATA[i]] = count
#
#     elif(DATA[i] != DATA[i+1] and DATA[i] in dict):
#         dict[DATA[i]] = count
#         count = 1
#
#     else:
#         count = 1
#         dict[DATA[i]] = count


# print(dict)
# print(third_table(DATA))
# interval_calculation(min_value=min(DATA), max_value=max(DATA), count_elements=len(DATA))
# print(check_step(270, DATA))
# print(interval_step_check(42, DATA, 42))
# print(find_divisors(42))

def forth_table(size_of_interval, count_of_steps):
    # self.dict_table_4 = {
    #     "i": [],
    #     "interval": [],
    #     "ni": [],
    #     "pi": []
    # }
    # number_elements = []
    # interval = []
    # ni = []
    # pi = []
    table = PrettyTable()
    table.field_names = ["i", 'Xi < X < Xi+1', 'ni', 'pi']
    unique_data_values = SORTED_DATA.copy()
    len_of_data = len(SORTED_DATA)
    min_value = unique_data_values[0]
    current_value = min_value
    max_value = unique_data_values[-1]
    number_of_element = 1
    count_of_element = 0  # Равно одному потому что изначально уже добавляю первый элемент из списка
    # del unique_data_values[0]  # Удаляю первый элемент из списка что бы все шло ровно
    for_a_crutch = unique_data_values[0]
    last_index_of_element = 0
    # print(f"i  |  Xi < X < Xi+1 | ni  |  pi |")
    for step in range(count_of_steps):
    # while current_value <= max_value:
        prev_value = current_value
        current_value += size_of_interval
        for i in range(last_index_of_element, len_of_data):
            if unique_data_values[i] == for_a_crutch:  # костыль чтобы у меня не удалялись лишние элементы доделать если пойму как можно сделать иначе
                count_of_element += 1
            elif prev_value < unique_data_values[i] <= current_value:
                count_of_element += 1
            else:

                # for j in range(0, count_of_element):
                #     del unique_data_values[0]
                last_index_of_element += count_of_element
                table.add_row([number_of_element, f'{prev_value} - {current_value}', count_of_element,
                               f'{count_of_element}/{len_of_data}'])

                count_of_element = 0
                break
        else:
            if number_of_element == count_of_steps:
                table.add_row([number_of_element, f'{prev_value} - {current_value}', count_of_element, f'{count_of_element}/{len_of_data}'])
        # number_elements.append(number_of_element)
        # interval.append([prev_value, current_value])
        # ni.append(count_of_element)
        # pi.append(count_of_element / len(self.data))

        number_of_element += 1

    print(table)

forth_table(331, 6)
print(len(SORTED_DATA))
print(len(DATA))
# for i in SORTED_DATA:
#     print(i)