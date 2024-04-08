from prettytable import PrettyTable
from math import log10
# DATA = [51, 89 ,51 ,18, 51 ,81 ,30 ,39, 4 ,31 ,51, 26, 39, 51 ,78 ,74 ,11 ,48 ,16 ,76 ,57 ,32 ,99 ,69 ,94 ,40 ,53 ,46 ,73 ,14 ,78 ,16 ,60 ,94 ,12 ,60 ,48 ,15, 86 ,17 ,27 ,15 ,28 ,31 ,36 ,99 ,33 ,17 ,42,14]
DATA = [1782, 1963, 1791, 1287, 1063, 1222, 1206, 1329, 1528, 1238, 1848, 1858, 1289, 1586, 772, 
        1266, 1242, 1816, 951, 1693, 1643, 1497, 1280, 1760, 1717, 1212, 1238, 1259, 1901, 1022, 
        818, 1894, 1972, 1216, 1973, 1595, 1324, 1206, 1136, 1111, 1670, 1765, 1517, 762, 2092, 
        1279, 1942, 437, 408, 995, 2101, 2132, 1100, 1235, 1036, 1264, 1275, 1386, 1652, 1760, 1308, 
        812, 1514, 1197, 1222, 1907, 1172, 1137, 1709, 1150, 1456, 1519, 1843, 1085, 1525, 1668, 981,
        1662, 1216, 1808, 146, 1098, 1917, 1492, 1510]
def first_table(data):

    # mas = list(map(int, input().split()))
    # mas = [51, 89 ,51 ,18, 51 ,81 ,30 ,39, 4 ,31 ,51, 26, 39, 51 ,78 ,74 ,11 ,48 ,16 ,76 ,57 ,32 ,99 ,69 ,94 ,40 ,53 ,46 ,73 ,14 ,78 ,16 ,60 ,94 ,12 ,60 ,48 ,15, 86 ,17 ,27 ,15 ,28 ,31 ,36 ,99 ,33 ,17 ,42,14]
    table = PrettyTable()
    table.field_names = ['№', 'X']    
    print(DATA)
    # 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306 195571 123456 456 667890 8101880650 35674755 357200 16142449 161629 19532306
    for i in range(0, len(data) - 1):
        table.add_row([i+1, data[i]])
        
    print("Выборочные данные X")
    print(table)
    
def second_table(data):
    table = PrettyTable()
    table.field_names = ['№', 'X']
    sortedData = sorted(data)
    for i in range(0, len(sortedData) - 1):
        table.add_row([i+1, sortedData[i]])
    print("Ранжированный ряд для велечины X\n(по увелечению X)")
    print(table)
    return sortedData

def third_table(data):
    list_poryad_nomer = []
    list_elem = []
    list_ni = []
    list_pi = []
    countOfNumber = 0
    data_without_repeat = set()
    table = PrettyTable()
    table.field_names = ['№', 'Xi', 'ni', 'pi']
    for i in range(0, len(data)-1):
        for j in range(0, len(data)-1):
            if(data[i] == data[j]):
                countOfNumber+=1 
                data_without_repeat.add(i)
                
        table.add_row([i+1, data[i], countOfNumber, f'{countOfNumber}/{len(data)}'])   
        list_poryad_nomer.append(i+1)
        list_elem.append(data[i])
        list_ni.append(countOfNumber)
        list_pi.append(f'{countOfNumber}/{len(data)}')
        countOfNumber = 0
    dictForSchet = {
        "i": list_poryad_nomer,
        "Xi": list_elem,
        "ni": list_ni,
        "pi": list_pi
    }
    return table, dictForSchet
        
   
def interval_calculation(*, min_value, max_value, count_elements):
    scope_of_ineterval = max_value - min_value
    size_of_ineterval = int((scope_of_ineterval)/(1 + 3.28*log10(count_elements)))
    print(scope_of_ineterval, size_of_ineterval)

def check_step(size_of_ineterval, elements):
    count = 146
    count_of_steps = 0
    max_element = max(elements)
    while(count <= max_element):
        count += size_of_ineterval 
        count_of_steps+=1
    return count > max_element, count, count_of_steps #Если шаг больше то возвращает true
    
def interval_step_check(size_of_ineterval, elements):
    # mass_of_intervals = []
    # item_number = 0
    # count = min(elements)
    # while(count <= max(elements)):
    #     count_prev = count
    #     count += size_of_ineterval
    #     mass_of_intervals.append(f"{count_prev} - {count}")
    #     print(mass_of_intervals)
    while(check_step(size_of_ineterval, elements)):
        
        
    # correct_size_interval = 
# print(max(DATA), min(DATA))
# interval_calculation(max_value=max(DATA), min_value = min(DATA), count_elements=len(DATA))

    
    
interval_step_check(270, second_table(DATA))
    
    
    
    
# first_table(DATA)
# second_table(DATA)