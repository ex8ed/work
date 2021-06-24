# -*- coding: utf-8 -*-
"""
Набор функций, позволяющих получить DataFrame-объекты
для составления графических и текстовых отчетов.
Содержит набор функций проверки формата.
"""

import pandas as pd
from tkinter import messagebox
from checking import chars, numerical, phone_number, data
import datetime


global children
global otdeli
global workers


def init_db():
    """
    Загрузка данных
    -------
    db - фрейм с данными
    """
    global children
    global otdeli
    global workers
    workers = pd.read_pickle('../data/workers.pic')
    children = pd.read_pickle('../data/children.pic')
    otdeli = pd.read_pickle('../data/otdeli.pic')


def load_default_text():
    """
    Returns
    -------
    default_text : str
    Загрузка текста для начального экрана
    """
    with open('./data/default_text.txt', 'r', encoding='utf-8') as f:
        default_text = f.read()
    return default_text


def load_info_text():
    """
    Returns
    -------
    info_text : str
    Загрузка текста с информацией о приложении
    """
    with open('./data/info_text.txt', 'r', encoding='utf-8') as f:
        info_text = f.read()
    return info_text


def load_help_text():
    """
    Returns
    -------
    help_text : str
    Загрузка текста со справкой по работе с приложением
    """
    with open('./data/help_text.txt', 'r', encoding='utf-8') as f:
        help_text = f.read()
    return help_text


def end(root):
    """
    Функция закрытия главного окна
    
    Parameters
    ----------
    root : tkinter.root
    Returns
    -------
    None.
    """
    root.destroy()


def return_dict(dict_name):
    """
    Parameters
    ----------
    dict_name : str
        Название справочника
    Returns
    -------
    TYPE pandas.dataframe либо None
        Возвращает соотвествующий справочник либо None
        если было введено некорректное название
    """
    if dict_name == 'Работники':
        return workers
    elif dict_name == 'Дети работников':
        return children
    elif dict_name == 'Отделы':
        return otdeli
    else:
        return None


def data_transfer(data_):
    """
        Функция приводит строку с указанной датой
    к временному типу.
    :param data_: строка
    :return: дата в формате datetime
    """
    d_t = data_.split('.')
    d_t.reverse()
    data_list = map(int, d_t)
    return datetime.datetime(*data_list)


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
    if False in [chars(fio), data(birth), chars(child), chars(vac), numerical(dep),
                 numerical(pay)]:
        messagebox.showerror("Error", "Данные введены некорректно")
    else:
        workers.loc[workers.index.max() + 1] = [fio, data_transfer(birth),
                                                child, vac, dep, prof, pay]
        save()
        messagebox.showinfo("Info", "Поле успешно добавлено")


def adding_to_children(fio, birth_ch, k_gard):
    """
    Добавляет строку в справочник children
    :param fio: ФИО Ребенка
    :param birth_ch: Дата рождения ребенка
    :param k_gard: Номер садика
    :return:
    """
    global children
    if False in [chars(fio), data(birth_ch), numerical(k_gard)]:
        messagebox.showerror("Error", "Данные введены некорректно!")
    else:
        children.loc[children.index.max() + 1] = [fio, data_transfer(birth_ch), k_gard]
        save()
        messagebox.showinfo("Info", "Поле успешно добавлено")


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
    else:
        otdeli.loc[otdeli.index.max() + 1] = [num,
                                              data_transfer(date), tel, num_workers]
        save()
        messagebox.showinfo("Info", "Поле успешно добавлено")


def deleting(dict_name, index):
    """
        Удаляет строку по индексу.
    Возвращает копию Dataframe.
    :param dict_name: наименование словаря
    :param index: индекс удаляемой строки
    :return: копия Dataframe без строки.
    """
    try:
        return_dict(dict_name).drop([index], inplace=False)
        messagebox.showinfo("Info", "Поле успешно удалено")
    except KeyError:
        messagebox.showerror("Error", "Индекс не найден")


def save():
    """
        Сохраняет копию объекта DataFrame
    в формате Pickle.
    """
    global workers
    global children
    global otdeli
    workers.to_pickle('./data/workers.pic')
    children.to_pickle('./data/children.pic')
    otdeli.to_pickle('./data/otdeli.pic')
    messagebox.showinfo("Info", "Сохранение прошло успешно")


def back_attr(dict_name, name):
    """
        Функция возвращает поле по имени заданного атрибута
    :param dict_name: наименование словаря
    :param name: Имя запрашиваемого атрибута
    :return: Объект DataFrame
    """
    try:
        db = return_dict(dict_name)[[name]]
        if db is not None:
            return db
        else:
            messagebox.showerror("Error", "Вызываемого справочника не существует")
    except KeyError:
        messagebox.showerror("Error", "Вызываемого поля не существует")


def back_named_col(dict_name, names):
    """
        Функция возвращает множество полей, по заданным атрибутам,
    если таковые имеются. (Предусмотрена проверка наличия набора)
    :param dict_name: наименование словаря
    :param names: строка из наборов атрибутов
    :return: Множество полей в объекте DataFrame
    """
    try:
        db = return_dict(dict_name)[[s.strip() for s in names.split(',')]]
        if db is not None:
            return db
        else:
            messagebox.showerror("Error", "Вызываемого справочника не существует")
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
        return db.loc[db[by_name] == int(condition),
                      [s.strip() for s in names.split(',')]]
    except AttributeError:
        messagebox.showerror("Error", "Вызываемого справочника не существует")
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
    if db is not None:
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
    else:
        messagebox.showerror("Error", "Вызываемого справочника не существует")


def remove_workers(index):
    """
    Функция удаления записи из справочника workers

    Parameters
    ----------
    index : int
    Returns
    -------
    None.
    """
    global workers
    workers = workers.drop(int(index)).reset_index(drop=True)
    save()


def remove_children(index):
    """
    Функция удаления записи из справочника children

    Parameters
    ----------
    index : int
    Returns
    -------
    None.
    """
    global children
    children = children.drop(int(index)).reset_index(drop=True)
    save()


def remove_otdeli(index):
    """
    Функция удаления записи из справочника otdeli

    Parameters
    ----------
    index : int
    Returns
    -------
    None.
    """
    global otdeli
    otdeli = otdeli.drop(int(index)).reset_index(drop=True)
    save()


def save_workers(index, fio, birth, child, vac, dep, prof, pay):
    """
    Функция добавления новой записи в справочник workers

    Parameters
    ----------
    index : int
    fio : str
    birth : str
    child : str
    vac : str
    dep : str
    prof : str
    pay : str

    Returns
    -------
    None.

    """
    global workers
    workers.loc[int(index), 'ФИО'] = fio
    workers.loc[int(index), 'Дата рождения'] = birth
    workers.loc[int(index), 'ФИО Ребенка'] = child
    workers.loc[int(index), 'Прививка от COVID-19'] = vac
    workers.loc[int(index), 'Номер отдела'] = float(dep)
    workers.loc[int(index), 'Должность'] = prof
    workers.loc[int(index), 'З/П в месяц'] = float(pay)
    save()


def save_children(index, fio, birth, garden):
    """
    Функция добавления новой записи в справочник children

    Parameters
    ----------
    index : int.
    fio : str
    birth : str
    garden : str

    Returns
    -------
    None.

    """
    global children
    children.loc[int(index), 'ФИО Ребенка'] = fio
    children.loc[int(index), 'Дата рождения ребенка'] = birth
    children.loc[int(index), 'Номер садика'] = garden
    save()


def save_otdeli(index, num, date, tel, num_workers):
    """
    Функция добавления новой записи в справочник otdeli

    Parameters
    ----------
    index : int
    num : str
    date : str
    tel : str
    num_workers : str

    Returns
    -------
    None.

    """
    global otdeli
    otdeli.loc[int(index), 'Номер отдела'] = num
    otdeli.loc[int(index), 'Дата создания'] = date
    otdeli.loc[int(index), 'Телефон'] = tel
    otdeli.loc[int(index), 'Количество сотрудников'] = num_workers
    save()


init_db()
