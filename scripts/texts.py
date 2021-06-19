# -*- coding: utf-8 -*-

"""
Набор функций, позволяющих получить DataFrame-объекты
для составления графических и текстовых отчетов.
Содержит набор функций проверки формата.

@author: Nick
"""


import pandas as pd


def back_attr(R, name):
    """
    @author: Nick
        Функция возвращает поле по имени заданного атрибута
    :param R: База данных
    :param name: Имя запрашиваемого атрибута
    :return: Объект DataFrame
    """
    return R[[name]].iterrows()


def back_named_col(R, names: tuple):
    """
    @author: Nick
        Функция возвращает множество полей, по заданным атрибутам,
    если таковые имеются. (Предусмотрена проверка наличия набора)
    :param R: База данных
    :param names: кортеж из наборов атрибутов
    :return: Множество полей в объекте DataFrame
    """
    return R[[*names]].iterrows()


def back_names_cond(R,
                    names: tuple,
                    by_name,
                    condition):
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
    return R.loc[R[by_name] == condition, [*names]].iterrows()


def back_many_cond(R,
                   names: tuple,
                   by_names: tuple,
                   conditions: tuple):
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
    cond0 = R[by_names[0]] == conditions[0]
    cond1 = R[by_names[1]] == conditions[1]
    return R.loc[cond0 & cond1, [*names]].iterrows()


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


# DB = pd.read_pickle('C:/Users/Nick/Documents/work/data/db.pic')

# самый простой вывод одного поля
# print(back_attr(DB, 'Номер работника'))

# выборка нескольких полей
# print(back_named_columns(DB, ('ФИО', 'ФИО Ребенка', 'Должность')))

# выборка по одному критерию нужных имен
# print(back_attr_with_condition(DB, ('ФИО', 'ФИО Ребенка'), 'Прививка от COVID-19', 'Да'))

# выборка по двум критериям для нужных имен
# print(back_many_cond(DB,
#                      ('ФИО', 'Дата рождения'),
#                      ('Прививка от COVID-19', 'Номер отдела'),
#                      ('Да', 2)
#                      )
#       )

# print(correct_number('+7-800-555-35-35'))
# print(correct_data('02.02.2020'))
