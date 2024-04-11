from matplotlib import pyplot as pp

def first_graph(os_x, os_y):
    pp.figure(figsize=(12, 4))
    pp.title("Эмпирическая функция распределения")
    x_list = os_x
    y_list = os_y
    pp.plot(x_list, y_list, marker = 'o')
    pp.show()

def second_graph(os_x, os_y, os_y1):
    pp.figure(figsize=(12, 4))
    pp.title("Эмпирические и теоритические частоты")
    x_list = os_x
    y_list = os_y
    y_list1 = os_y1
    pp.plot(x_list, y_list, marker = 'o')
    pp.plot(x_list, y_list1, marker = 'o')
    pp.show()

def third_graph(os_x, os_y):
    x_list = os_x
    y_list = os_y

    width = 0.3
    figsize = [6.4, 4.8]

    if 6 < len(x_list) >= 10:
        figsize = [12, 4]
        width = 2

    pp.figure(figsize=(figsize[0], figsize[1]))

    pp.bar(x_list, y_list, width=width)
    pp.title("Гистограмма итегрального вариационного ряда")
    pp.xticks(x_list, x_list)
    pp.show()