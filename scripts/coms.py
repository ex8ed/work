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

global children
global otdeli
global workers
global db


def chars(string):
    if ''.join(string.split()).isalpha():
        return string
    return False


def numerical(string):
    if string.strip().isdigit():
        return string
    return False


def correct_number(number):
    """
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


def load():
    """
    Загрузка данных
    -------
    db - фрейм с данными
    """
    global children
    global otdeli
    global workers
    global db
    f_types = [('Pickle файлы', '*.pic'), ('Все файлы', '*')]
    dlg = fld.Open(filetypes=f_types)
    fl = dlg.show()
    if len(fl) != 0:
        db = pd.read_pickle('./data/db.pic')
        workers = pd.read_pickle('./data/workers.pic')
        children = pd.read_pickle('./data/children.pic')
        otdeli = pd.read_pickle('./data/otdeli.pic')
        messagebox.showinfo('Info page', 'Файл открыт успешно')
    pass


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


def return_path(dict_name):
    if dict_name == 'Работники':
        return './data/workers.pic'
    elif dict_name == 'Дети работников':
        return './data/children.pic'
    elif dict_name == 'Отделы':
        return './data/otdeli.pic'


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
    if False in [chars(fio), correct_data(birth), chars(child), chars(vac), numerical(dep),
                 numerical(pay)]:
        print([chars(fio), correct_data(birth), chars(child), chars(vac), numerical(dep),
               numerical(pay)])
        messagebox.showerror("Error", "Данные введены некорректно!")
        return False
    else:
        workers.loc[workers.index.max() + 1] = [fio, birth, child, vac, dep, prof, pay]
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
    print([chars(fio), correct_data(birth_ch), numerical(k_gard)])
    if False in [chars(fio), correct_data(birth_ch), numerical(k_gard)]:
        messagebox.showerror("Error", "Данные введены некорректно!")
        return False
    else:
        children.loc[children.index.max() + 1] = [fio, birth_ch, k_gard]


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
    if False in [numerical(num), correct_data(date), correct_number(tel), numerical(num_workers)]:
        messagebox.showerror("Error", "Неверный формат данных")
        return False
    else:
        otdeli.loc[otdeli.index.max() + 1] = [num, date, tel, num_workers]


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
    workers.to_pickle(path + '/data/workers.pic')
    children.to_pickle(path + '/data/children.pic')
    otdeli.to_pickle(path + '/data/otdeli.pic')
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


def scatter():
    """
    Рассеянная диаграмма зарплат работников по возрасту
    """
    global workers
    salary = workers['З/П в месяц'].values
    for y, x in enumerate(workers['Дата рождения'].values):
        plt.scatter((2020 - int(str(x).split('-')[0])), salary[y], color='Blue')
    plt.title('Распределение зарплаты по возрастам')
    plt.show()


def bar_covid():
    """
    Столбчатая диаграмма вакцинированных и невакцинированных от COVID-19
    """
    global workers
    vaccinated = workers[workers['Прививка от COVID-19'] == 'Да'].shape[0]
    not_vaccinated = workers[workers['Прививка от COVID-19'] == 'Нет'].shape[0]
    plt.bar(['Да', 'Нет'], [vaccinated, not_vaccinated])
    plt.title('Вакцинация от COVID-19')
    plt.show()


def bar_sadik():
    """
    Столбчатая диаграмма распределения детей по садикам
    """
    global children
    children_aggregated = children.groupby('Номер садика').agg({'Дата рождения ребенка': 'count'}).reset_index()
    plt.bar(children_aggregated['Номер садика'], children_aggregated['Дата рождения ребенка'])
    plt.yticks([3, 6, 9, 12, 15, 18, 21])
    plt.title('Распределение детей по садикам')
    plt.show()


def bar_otdel_salary():
    """
    Столбчатая диаграмма средней зп по отделам
    """
    global workers
    workers_aggregated = workers.groupby('Номер отдела').agg({'З/П в месяц': 'mean'}).reset_index()
    plt.bar(workers_aggregated['Номер отдела'], workers_aggregated['З/П в месяц'])
    plt.xticks([1, 2, 3])
    plt.title('Средняя зп по отделам')
    plt.show()


def bar_otdeli():
    """
    Столбчатая диаграмма распределения сотрудников по отделам
    """
    global otdeli
    plt.bar(otdeli['Номер отдела'], otdeli['Количество сотрудников'])
    plt.title('Распределение сотрудников по отделам')
    plt.xticks([1, 2, 3])
    plt.show()


def hist_salary():
    """
    Гистограмма распределения зарплат рабочих
    """
    global workers
    workers['З/П в месяц'].hist()
    plt.title('Распределение зарплат рабочих')
    plt.show()


def hist_birth_workers():
    """
    Гистограмма распределения рабочих по годам рождения
    """
    global workers
    workers['Дата рождения'].hist()
    plt.title('Распределение рабочих по годам рождения')
    plt.show()


def hist_birth_children():
    """
    Гистограмма распределения детей по годам рождения
    """
    global children
    children['Дата рождения ребенка'].hist()
    plt.title('Распределение детей по годам рождения')
    plt.show()


def make_plot(dictionary, graph_type, num):
    if dictionary == 'Работники':
        if graph_type == 'Гистограмма':
            if num == 'Гистограмма распределения рабочих по годам рождения':
                hist_birth_workers()
            elif num == 'Гистограмма распределения зарплат рабочих':
                hist_salary()
        elif graph_type == 'Столбчатая диаграмма':
            if num == 'Столбчатая диаграмма средней зп по отделам':
                bar_otdel_salary()
            elif num == 'Столбчатая диаграмма вакцинированных и невакцинированных от COVID-19':
                bar_covid()
        else:
            scatter()
    elif dictionary == 'Дети работников':
        if graph_type == 'Гистограмма':
            hist_birth_children()
        elif graph_type == 'Столбчатая диаграмма':
            bar_sadik()
    else:
        if graph_type == 'Столбчатая диаграмма':
            bar_otdeli()
