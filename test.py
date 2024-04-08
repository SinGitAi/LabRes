from tables import Tables
DATA = [27, 27, 29, 29, 29, 31, 31, 31, 33, 33, 34, 34, 34, 34, 35, 35, 35, 35, 35, 36, 36, 36,
         36, 36, 37, 37, 37, 37, 37, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 41, 41, 41,
         41, 41, 41, 42, 43, 43, 43, 44, 44, 44, 44, 45, 45, 46, 47, 47, 48, 49, 49, 50, 50, 51,
         52, 52, 54, 54, 55, 57, 58, 59, 69, 77, 89, 89, 90, 90, 95, 99, 108, 116, 123]
tables = Tables(DATA)
# first_table = tables.selecting_and_printing_table(1)
# first_table_values = tables.selecting_and_geting_value_of_table(1)
# print(first_table_values)
# second_table = tables.selecting_and_printing_table(2)
# second_table_values = tables.selecting_and_geting_value_of_table(2)
# print(second_table_values)
third_table = tables.selecting_and_printing_table(3)
third_table_values = tables.selecting_and_geting_value_of_table(3)
print(third_table_values)
