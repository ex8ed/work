# -*- coding: utf-8 -*-
"""
Набор функций, позволяющих получить DataFrame-объекты
для составления графических и текстовых отчетов.
Содержит набор функций проверки формата.
"""
import os
import pandas as pd
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter import filedialog as fld
from checking import chars, numerical, phone_number, data

def init_db():
    """
    Загрузка данных
    -------
    db - фрейм с данными
    """
    global children
    global otdeli
    global workers
    global db
    db = pd.read_pickle('../data/db.pic')
    workers = pd.read_pickle('../data/workers.pic')
    children = pd.read_pickle('../data/children.pic')
    otdeli = pd.read_pickle('../data/otdeli.pic')

def get_workers():
    return workers


def get_children():
    return children


def get_deps():
    return otdeli


def end(root):
    root.destroy()


def return_dict(dict_name):
    global children
    global otdeli
    global workers
    if dict_name == 'Работники':
        return workers
    elif dict_name == 'Дети работников':
        return children
    elif dict_name == 'Отделы':
        return otdeli

def adding_to_workers(fio, birth, child, vac, dep, prof, pay):
    """
    Добавляет строку в справочник workers
    :param fio:  ФИО
    :param birth: Дата рождения
    :param child: ФИО Ребенка
    :param vac: Наличие прививки
    :param dep: Номер отдела
    :param prof: Должность
    :param pay: Заработная плата
    :return:
    """
    global workers
    print(fio)
    if False in [chars(fio), data(birth), chars(child), chars(vac), numerical(dep),
                 numerical(pay)]:
        print([chars(fio), data(birth), chars(child), chars(vac), numerical(dep),
               numerical(pay)])
        messagebox.showerror("Error", "Данные введены некорректно!")
        return False
    else:
        workers.loc[workers.index.max() + 1] = [fio, birth, child, vac, dep, prof, pay]
        save()
        return False


def adding_to_children(fio, birth_ch, k_gard):
    """
    Добавляет строку в справочник children
    :param fio: ФИО Ребенка
    :param birth_ch: Дата рождения ребенка
    :param k_gard: Номер садика
    :return:
    """
    global children
    print([chars(fio),data(birth_ch), numerical(k_gard)])
    if False in [chars(fio), data(birth_ch), numerical(k_gard)]:
        messagebox.showerror("Error", "Данные введены некорректно!")
        return False
    else:
        children.loc[children.index.max() + 1] = [fio, birth_ch, k_gard]
        save()


def adding_to_otdeli(num, date, tel, num_workers):
    """
    Добавляет строку в справочник otdeli
    :param num: номер
    :param date: дата создания отдела
    :param tel: номер телефона
    :param num_workers: Количество работников
    :return:
    """
    global otdeli
    if False in [numerical(num), data(date), phone_number(tel), numerical(num_workers)]:
        messagebox.showerror("Error", "Неверный формат данных")
        return False
    else:
        otdeli.loc[otdeli.index.max() + 1] = [num, date, tel, num_workers]
        save()


def deleting(dict_name, index):
    """
        Удаляет строку по индексу.
    Возвращает копию Dataframe.
    :param dict_name: наименование словаря
    :param index: индекс удаляемой строки
    :return: копия Dataframe без строки.
    """
    print(index)
    try:
        return_dict(dict_name).drop([index], inplace=False)
    except KeyError:
        messagebox.showerror("Error", "Индекс не найден")


def save():
    """
        Сохраняет копию объекта DataFrame
    в формате Pickle.
    :param dict_name: наименование словаря
    :param obj: полученный объект
    :return:
    """
    global workers
    global children
    global otdeli
    path = os.getcwd()
    return 0


def back_attr(dict_name, name):
    """
        Функция возвращает поле по имени заданного атрибута
    :param dict_name: наименование словаря
    :param name: Имя запрашиваемого атрибута
    :return: Объект DataFrame
    """
    try:
        return return_dict(dict_name)[[name]]
    except KeyError:
        messagebox.showerror("Error", "Вызываемого поля не существует")


def back_named_col(dict_name, names):
    """
        Функция возвращает множество полей, по заданным атрибутам,
    если таковые имеются. (Предусмотрена проверка наличия набора)
    :param dict_name: наименование словаря
    :param names: кортеж из наборов атрибутов
    :return: Множество полей в объекте DataFrame
    """
    try:
        return return_dict(dict_name)[[s.strip() for s in names.split(',')]]
    except KeyError:
        messagebox.showerror("Error", "Вызываемого поля не существует")


def back_names_cond(dict_name, names, by_name, condition):
    """
        Функция возвращает поля атрибутов names если параметр
        by_name удовлетворяет condition.
    :param dict_name: наименование словаря
    :param names: имена выводимых атрибутов
    :param by_name: имя атрибута, по которому происходит сравнение
    :param condition: условие для проверки по объекту by_name
    :return: набор атрибутов в объекте DataFrame
    """
    db = return_dict(dict_name)
    try:
        db = return_dict(dict_name)
        return db.loc[db[by_name] == int(condition),
                      [s.strip() for s in names.split(',')]]
    except ValueError:
        return db.loc[db[by_name] == condition,
                      [s.strip() for s in names.split(',')]]
    except KeyError:
        messagebox.showerror("Error", "Вызываемого поля не существует")


def back_many_cond(dict_name, names, by_names: str, conditions: str):
    """
        Функция возвращает поля атрибутов names если параметры:
    by_name[i] удовлетворяет condition[i] (len = 2)
    :param conditions: Набор условий
    :param dict_name: наименование словаря
    :param names: имена выводимых атрибутов
    :param by_names: набор имен, по которым происходит отбор соотв. условия из conditions
    :param conditions: набор условий для каждого i-того имени
    :return:
    """
    db = return_dict(dict_name)
    cond = [s.strip() for s in conditions.split(',')]
    b_n = [s.strip() for s in by_names.split(',')]
    # Проверка на числовые параметры
    try:
        cond0 = db[b_n[0]] == int(cond[0])
    except ValueError:
        cond0 = db[b_n[0]] == cond[0]

    try:
        cond1 = db[b_n[1]] == int(cond[1])
    except ValueError:
        cond1 = db[b_n[1]] == cond[1]
    try:
        return db.loc[cond0 & cond1, [s.strip() for s in names.split(',')]]
    except KeyError:
        messagebox.showerror("Error", "Вызываемого поля не существует")

def remove_workers(index):
    global workers
    workers = workers.drop(int(index)).reset_index(drop=True)
    save()

def remove_children(index):
    global children
    children = children.drop(int(index)).reset_index(drop=True)
    save()

def remove_otdeli(index):
    global otdeli
    otdeli = otdeli.drop(int(index)).reset_index(drop=True)
    save()

def save_workers(index, fio, birth, child, vac, dep, prof, pay):
    global workers
    workers.loc[int(index), 'ФИО'] = fio
    workers.loc[int(index), 'Дата рождения'] = birth
    workers.loc[int(index), 'ФИО Ребенка'] = child
    workers.loc[int(index), 'Прививка от COVID-19'] = vac
    workers.loc[int(index), 'Номер отдела'] = dep
    workers.loc[int(index), 'Должность'] = prof
    workers.loc[int(index), 'З/П в месяц'] = pay
    save()

def save_children(index, fio, birth, garden):
    global children
    children.loc[int(index), 'ФИО Ребенка'] = fio
    children.loc[int(index), 'Дата рождения ребенка'] = birth
    children.loc[int(index), 'Номер садика'] = garden
    save()

def save_otdeli(index, num, date, tel, num_workers):
    global otdeli
    otdeli.loc[int(index), 'Номер отдела'] = num
    otdeli.loc[int(index), 'Дата создания'] = date
    otdeli.loc[int(index), 'Телефон'] = tel
    otdeli.loc[int(index), 'Количество сотрудников'] = num_workers
    save()

#FIX ME! 
init_db()
