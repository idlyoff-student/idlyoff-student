from math import *

def f1(a, x):
    y = (tan(x**2 / 2 - 1)**2 + (2 * cos(x - pi / 6)) / (1 / 2 + sin(a)**2))
    return y

def f2(x):
    y = pow(2, log(3 - cos(pi / 4 + 2 * x), 3 + sin(x)) / (1 + tan(2 * x / pi)**2))
    return y

fi = open("lab1_pb_in.txt", "rt")
fo = open("lab1_pb_ou.txt", "wt")

line = fi.readline()  # Пропустить заголовок в файле
# Вывести шапку таблицы в файл
fo.write("+======+======+=========+========+\n")
fo.write("I A I X I F1 I F2 I\n")
fo.write("+======+======+=========+========+\n")

for line in fi:  # Для всех строк файла
    if line == "\n":
        continue
    (b, c) = line.split()  # Расщепить
    a = float(b)  # Привести к вещественному типу
    x = float(c)
    # Вывод в файл
    fo.write("I {0: .1f} I {1: .1f} I {2: 5.4f} I".format(a, x, f1(a, x)))
    fo.write("{0: 6.4f} I\n".format(f2(x)))
    fo.write("+------+------+---------+--------+\n")

fi.close()  # Закрываем файлы
fo.close()
