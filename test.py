from tables import Tables
from formuls_calculation_functions import IntervalCalculation
import graphs
DATA = [1782, 1963, 1791, 1287, 1063, 1222, 1206, 1329, 1528, 1238, 1848, 1858, 1289, 1586, 772,
        1266, 1242, 1816, 951, 1693, 1643, 1497, 1280, 1760, 1717, 1212, 1238, 1259, 1901, 1022,
        818, 1894, 1972, 1216, 1973, 1595, 1324, 1206, 1136, 1111, 1670, 1765, 1517, 762, 2092,
        1279, 1942, 437, 408, 995, 2101, 2132, 1100, 1235, 1036, 1264, 1275, 1386, 1652, 1760, 1308,
        812, 1514, 1197, 1222, 1907, 1172, 1137, 1709, 1150, 1456, 1519, 1843, 1085, 1525, 1668, 981,
        1662, 1216, 1808, 146, 1098, 1917, 1492, 1510]
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

tables = Tables(DATA)
# first_table = tables.selecting_and_printing_table(1)
# first_table_values = tables.selecting_and_geting_value_of_table(1)
# print(first_table_values)
second_table = tables.selecting_and_printing_table(2)
second_table_values = tables.selecting_and_geting_value_of_table(2)
# print(second_table_values)
# Расчет 3 табоицы возможен только после расчета 2 таблицы
third_table = tables.selecting_and_printing_table(3)
# third_table_values = tables.selecting_and_geting_value_of_table(3)
# print(third_table_values["Xi"])
interval = IntervalCalculation(second_table_values)
size_of_interval, count_of_steps = interval.interval_calculation()
forth_table = tables.selecting_and_printing_table(4, size_of_interval, count_of_steps)
# forth_table_values = tables.selecting_and_geting_value_of_table(4)
# fifth_table = tables.selecting_and_printing_table(5)
# fifth_table_values = tables.selecting_and_geting_value_of_table(5)
sixth_table = tables.selecting_and_printing_table(6, size_of_interval)
# sixth_table_values = tables.selecting_and_geting_value_of_table(6)
seventh_table = tables.selecting_and_printing_table(7, size_of_interval)
# seventh_table_values = tables.selecting_and_geting_value_of_table(7)
eighth_table = tables.selecting_and_printing_table(8)

# graphs.first_graph(sixth_table_values['Xi'], fifth_table_values)
# graphs.second_graph(sixth_table_values['Xi'], sixth_table_values["pi*"], seventh_table_values["pi"])
# graphs.third_graph(sixth_table_values['Xi'], sixth_table_values['density'])






