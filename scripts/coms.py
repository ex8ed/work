import time
import re
import pandas as pd
from tkinter import filedialog as fld


def chars(string):
    if ''.join(string.split()).isalpha():
        return string
    return False


def numerical(string):
    if string.strip().isdigit():
        return string
    return False


def data(string):
    try:
        time.strptime(string, '%d.%m.%Y')
        return string
    except ValueError:
        return False


def phone_num(string):
    phone = re.sub(r'\b\D', '', string)
    clear_phone = re.sub(r'[\ \(]?', '', phone)
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$', string):
        return string
    return False


def load():
    """
    Загрузка данных

    Returns
    -------
    db - фрейм с данными

    """
    global db
    ftypes = [('Pickle файлы', '*.pic'), ('Все файлы', '*')]
    dlg = fld.Open(filetypes=ftypes)
    fl = dlg.show()
    if len(fl) != 0:
        db = pd.read_excel(fl)
    return 0


def end(root):
    root.destroy()


def adding(fio, birth, child, vac, dep, prof, pay):
    global db
    if False in [chars(fio), data(birth), chars(child), chars(vac), numerical(dep),
                 numerical(pay)]:
        return False
    else:
        db.loc[db.index.max() + 1] = [fio, birth, child, vac, dep, prof, pay]
        return False


def deleting():
    pass


# -*- coding: utf-8 -*-

"""
Набор функций, позволяющих получить DataFrame-объекты
для составления графических и текстовых отчетов.
Содержит набор функций проверки формата.

@author: Nick
"""


def back_attr(name):
    global db
    """
    @author: Nick
        Функция возвращает поле по имени заданного атрибута
    :param R: База данных
    :param name: Имя запрашиваемого атрибута
    :return: Объект DataFrame
    """
    return db[[name]]


def back_named_col(names):
    global db
    """
    @author: Nick
        Функция возвращает множество полей, по заданным атрибутам,
    если таковые имеются. (Предусмотрена проверка наличия набора)
    :param R: База данных
    :param names: кортеж из наборов атрибутов
    :return: Множество полей в объекте DataFrame
    """
    return db[names.split(',')]


def back_names_cond(names,
                    by_name,
                    condition):
    global db
    """
    @author: Nick
        Функция возвращает поля атрибутов names если параметр
        by_name удовлетворяет condition.
    :param R: база данных
    :param names: имена выводимых атрибутов
    :param by_name: имя атрибута, по которому происходит сравнение
    :param condition: условие для проверки по объекту by_name
    :return: набор атрибутов в объекте DataFrame
    """
    try:
        return db.loc[db[by_name] == int(condition), names]
    except:
        return db.loc[db[by_name] == int(condition), names]


def back_many_cond(names,
                   by_names: tuple,
                   conditions: tuple):
    global db
    """
    @author: Nick
        Функция возвращает поля атрибутов names если параметры:
    by_name[i] удовлетворяет condition[i] (len = 2)
    :param conditions: Набор условий
    :param R: База данных
    :param names: имена выводимых атрибутов
    :param by_names: набор имен, по которым происходит отбор соотв. условия из conditions
    :param conditions: набор условий для каждого i-того имени
    :return:
    """
    cond0 = db[by_names[0]] == conditions[0]
    cond1 = db[by_names[1]] == conditions[1]
    return db.loc[cond0 & cond1, names.split(',').strip()]


def correct_number(number):
    """
    @author: Nick
        Функция проверяет корректность
        введенного в справочник номера телефона
    :param number: данный номер телефона
    :return: Логическая константа-ответ.
    """
    if number[0] == '+' and len(number) >= 12:
        E_G = number[1:].replace('-', '')
        try:
            int(E_G)
            return True
        except ValueError:
            print("Unuseful number format")
            return False
    else:
        return False


def correct_data(data_str):
    """
    @author: Nick
        Функция проверяет корректность
        введенной в справочник даты.
    :param data_str: строка, содержащая дату
    :return: логическая константа-ответ
    """
    if len(data_str) == 10:
        E_G = data_str.replace('.', '')
        try:
            int(E_G)
            return True
        except ValueError:
            print("Unuseful data format.")
            return False
    else:
        return False
