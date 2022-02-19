import pandas
import random

robot_table = pandas.read_excel('sheet.xlsx', sheet_name='Sheet1')
group_table = pandas.read_excel('group.xlsx', sheet_name='Лист1')

students = group_table['amogus'].tolist()
students.pop(0)
for i in range(4):
    students.pop(23)

use_table = robot_table['Сфера'].tolist()
industrial_bin_table = robot_table['Промышленные роботы'].tolist()
transport_bin_table = robot_table['Транспортные роботы'].tolist()
military_bin_table = robot_table['Военные роботы'].tolist()
research_bin_table = robot_table['Исследовательские роботы'].tolist()
repair_bin_table = robot_table['Ремонтные роботы'].tolist()
sport_bin_table = robot_table['Спортивные роботы'].tolist()
var_sum_table = []


def choose1():
    r = random.randint(1, 6)
    if r == 1:
        f.write('промышленный робот, ')
        var_sum_table.append('1')
        return industrial_bin_table
    elif r == 2:
        f.write('транспортный робот, ')
        var_sum_table.append('2')
        return transport_bin_table
    elif r == 3:
        f.write('военный робот, ')
        var_sum_table.append('3')
        return military_bin_table
    elif r == 4:
        f.write('исследовательский робот, ')
        var_sum_table.append('4')
        return research_bin_table
    elif r == 5:
        f.write('ремонтный робот, ')
        var_sum_table.append('5')
        return repair_bin_table
    elif r == 6:
        f.write('спортивный робот, ')
        var_sum_table.append('6')
        return sport_bin_table
    else: choose1()


def choose2(i, bin_table):
    r = random.randint(1, 8)
    if (r == 1 and bin_table[0] == 1):
        f.write('гидросфера в толще, ')
        var_sum_table[i] += '1'
    elif (r == 2 and bin_table[1] == 1):
        f.write('водная поверхность, ')
        var_sum_table[i] += '2'
    elif (r == 3 and bin_table[2] == 1):
        f.write('геосфера в толще, ')
        var_sum_table[i] += '3'
    elif (r == 4 and bin_table[3] == 1):
        f.write('земная поверхность, ')
        var_sum_table[i] += '4'
    elif (r == 5 and bin_table[4] == 1):
        f.write('атмосфера до 3000 м, ')
        var_sum_table[i] += '5'
    elif (r == 6 and bin_table[5] == 1):
        f.write('атмосфера от 3000 м до 15000 м, ')
        var_sum_table[i] += '6'
    elif (r == 7 and bin_table[6] == 1):
        f.write('верхние слои атмосферы, ')
        var_sum_table[i] += '7'
    elif (r == 8 and bin_table[7] == 1):
        f.write('околоземное пространство, ')
        var_sum_table[i] += '8'
    else: choose2(i, bin_table)


def choose3(i, bin_table):
    r = random.randint(1, 7)
    if (r == 1 and bin_table[9] == 1):
        f.write('наноробот 10^-9 м, ')
        var_sum_table[i] += '1'
    elif (r == 2 and bin_table[10] == 1):
        f.write('микробот 10^-3 м , ')
        var_sum_table[i] += '2'
    elif (r == 3 and bin_table[11] == 1):
        f.write('миниатюрный робот  0.2 м, ')
        var_sum_table[i] += '3'
    elif (r == 4 and bin_table[12] == 1):
        f.write('маленький робот до 1м, ')
        var_sum_table[i] += '4'
    elif (r == 5 and bin_table[13] == 1):
        f.write('средний робот до 5м, ')
        var_sum_table[i] += '5'
    elif (r == 6 and bin_table[14] == 1):
        f.write('большой робот до 10 м, ')
        var_sum_table[i] += '6'
    elif (r == 7 and bin_table[15] == 1):
        f.write('сверхбольшой робот от 10 м, ')
        var_sum_table[i] += '7'
    else: choose3(i, bin_table)


def choose4(i, bin_table):
    r = random.randint(1, 3)
    if (r == 1 and bin_table[17] == 1):
        f.write('стационарный, ')
        var_sum_table[i] += '1'
    elif (r == 2 and bin_table[18] == 1):
        f.write('смешанный, ')
        var_sum_table[i] += '2'
    elif (r == 3 and bin_table[19] == 1):
        f.write('мобильный, ')
        var_sum_table[i] += '3'
    else: choose4(i, bin_table)


def choose5(i, bin_table):
    r = random.randint(1, 3)
    if (r == 1 and bin_table[21] == 1):
        f.write('программное управление, ')
        var_sum_table[i] += '1'
    elif (r == 2 and bin_table[22] == 1):
        f.write('адаптивное управление, ')
        var_sum_table[i] += '2'
    elif (r == 3 and bin_table[23] == 1):
        f.write('интеллектуальное управление, ')
        var_sum_table[i] += '3'
    else: choose5(i, bin_table)


def choose6(i, bin_table):
    r = random.randint(1, 4)
    if (r == 1 and bin_table[25] == 1):
        f.write('электрический привод, ')
        var_sum_table[i] += '1'
    elif (r == 2 and bin_table[26] == 1):
        f.write('гидравлический привод, ')
        var_sum_table[i] += '2'
    elif (r == 3 and bin_table[27] == 1):
        f.write('пневматический привод, ')
        var_sum_table[i] += '3'
    elif (r == 4 and bin_table[28] == 1):
        f.write('прочий тип привода, ')
        var_sum_table[i] += '4'
    else: choose6(i, bin_table)


def choose7(i, bin_table):
    r = random.randint(1, 4)
    if (r == 1 and bin_table[30] == 1):
        f.write('шагающая ходовая часть.')
        var_sum_table[i] += '1'
    elif (r == 2 and bin_table[31] == 1):
        f.write('гусеничная ходовая часть.')
        var_sum_table[i] += '2'
    elif (r == 3 and bin_table[32] == 1):
        f.write('колёсная ходовая часть.')
        var_sum_table[i] += '3'
    elif (r == 4 and bin_table[33] == 1):
        f.write('гибридная ходовая часть.')
        var_sum_table[i] += '4'
    else: choose7(i, bin_table)

counter = 0
for j in students:
    f = open('text.txt', 'a')
    f.write(j + ' - ')
    arr = choose1()
    choose2(counter, arr)
    choose3(counter, arr)
    choose4(counter, arr)
    choose5(counter, arr)
    choose6(counter, arr)
    choose7(counter, arr)

    flag = 0
    for i in range(len(var_sum_table) - 1):
        if var_sum_table[i] == len(var_sum_table):
            flag = 1
    if flag == 1:
        counter -= 1
        var_sum_table.pop(len(var_sum_table))

    counter += 1
    f.write('\n\n')
print(var_sum_table)
