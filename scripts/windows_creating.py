# -*- coding: utf-8 -*-
"""
Набор функций для генерации окон приложения.

"""

import tkinter as tk
import numpy as np
from tkinter import ttk
from coms import adding, deleting, back_attr, back_named_col, back_names_cond, back_many_cond


def add_combo(content,
              box_name="workers"):
    """
    Создает combobox для нужного справочника
    :param content: Объект TK
    :param box_name: имя справочника
    """
    if box_name == "workers":
        return ttk.Combobox(content,
                            values=["ФИО",
                                    "Дата рождения",
                                    "ФИО Ребенка",
                                    "Прививка от COVID-19",
                                    "Номер отдела",
                                    "Должность",
                                    "З/П в месяц"])
    elif box_name == "children":
        return ttk.Combobox(content,
                            values=["ФИО Ребенка",
                                    "Дата рождения ребенка",
                                    "Номер садика"])
    elif box_name == "otdeli":
        return ttk.Combobox(content,
                            values=["Дата создания",
                                    "Телефон",
                                    "Количество сотрудников"])


def add_row(content):
    """
    Создание окна для добавления записи в исходную базу данных
    """
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Добавление, редактирование и удаление записей')
    fio_label = tk.Label(content, text='ФИО')
    birth_label = tk.Label(content, text='Дата рождения')
    child_label = tk.Label(content, text='ФИО ребенка')
    vac_label = tk.Label(content, text='Был ли вакцинирован')
    dep_label = tk.Label(content, text='Номер департамента')
    prof_label = tk.Label(content, text='Проффессия')
    pay_label = tk.Label(content, text='Зарплата')
    fio_entry = ttk.Entry(content, width=40)
    birth_entry = ttk.Entry(content, width=40)
    child_entry = ttk.Entry(content, width=40)
    vac_entry = ttk.Entry(content, width=40)
    dep_entry = ttk.Entry(content, width=40)
    prof_entry = ttk.Entry(content, width=40)
    pay_entry = ttk.Entry(content, width=40)
    add = tk.Button(content, text='Добавить запись', width=20, command=lambda: adding(
        fio_entry.get(), birth_entry.get(), child_entry.get(), vac_entry.get(),
        dep_entry.get(), prof_entry.get(), pay_entry.get(),
    ))
    update = tk.Button(content, text='Обновить запись', width=20)
    delete = tk.Button(content, text='Удалить запись', width=20, command=deleting)

    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    fio_label.grid(column=0, row=1)
    birth_label.grid(column=0, row=2)
    child_label.grid(column=0, row=3)
    vac_label.grid(column=0, row=4)
    dep_label.grid(column=0, row=5)
    prof_label.grid(column=0, row=6)
    pay_label.grid(column=0, row=7)
    fio_entry.grid(column=3, row=1, columnspan=2)
    birth_entry.grid(column=3, row=2, columnspan=2)
    child_entry.grid(column=3, row=3, columnspan=2)
    vac_entry.grid(column=3, row=4, columnspan=2)
    dep_entry.grid(column=3, row=5, columnspan=2)
    prof_entry.grid(column=3, row=6, columnspan=2)
    pay_entry.grid(column=3, row=7, columnspan=2)
    add.grid(column=3, row=9, columnspan=2)
    update.grid(column=3, row=10, columnspan=2)
    delete.grid(column=3, row=11, columnspan=2)


def one_attr_search(rt, content):
    """
    Создание окна для поиска по одному атрибуту
    """

    for widget in content.winfo_children():
        widget.destroy()

    t = tk.Text(content, width=70, height=30)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set
    t.insert(1.0, 'Здесь будет выводится текст отчета')

    df = tk.StringVar()
    attr = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по одному атрибуту')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибут')

    # добавлены ComboBox
    df_entry = ttk.Combobox(content,
                            values=["workers",
                                    "children",
                                    "otdeli"])
    attr_entry = add_combo(content,
                           box_name=df_entry.get())

    button = tk.Button(content,
                       text='Вывести',
                       command=lambda: create_otchet_window(rt, back_attr(attr_entry.get())))

    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_entry.grid(column=1, row=1)
    attr_label.grid(column=0, row=2)
    attr_entry.grid(column=1, row=2)
    button.grid(column=0, row=3)
    xs.grid(column=0, row=7, sticky='we', columnspan=3)
    ys.grid(column=3, row=4, sticky='ns', rowspan=3)
    t.grid(column=0, row=4, sticky='nwes', columnspan=3, rowspan=3)
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(0, weight=1)


def many_attr_search(rt, content):
    """
    Создание окна для поиска по нескольким атрибутам
    """

    for widget in content.winfo_children():
        widget.destroy()

    t = tk.Text(content, width=70, height=30)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set
    t.insert(1.0, 'Здесь будет выводится текст отчета')

    df = tk.StringVar()
    attr = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибуты писать через запятую')

    df_entry = ttk.Entry(content, textvariable=df, width=45)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)

    button = tk.Button(content, text='Вывести',
                       command=lambda: create_otchet_window(rt, back_named_col(attr_entry.get())))

    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_entry.grid(column=1, row=1)
    attr_label.grid(column=0, row=2)
    attr_entry.grid(column=1, row=2)
    button.grid(column=0, row=3)
    xs.grid(column=0, row=7, sticky='we', columnspan=3)
    ys.grid(column=3, row=4, sticky='ns', rowspan=3)
    t.grid(column=0, row=4, sticky='nwes', columnspan=3, rowspan=3)
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(0, weight=1)


def one_attr_search_filter(rt, content):
    """
    Создание окна для поиска по одному атрибуту и условию
    """

    for widget in content.winfo_children():
        widget.destroy()

    t = tk.Text(content, width=70, height=30)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set
    t.insert(1.0, 'Здесь будет выводится текст отчета')

    df = tk.StringVar()
    attr = tk.StringVar()
    filt = tk.StringVar()
    val = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибуты (писать через запятую)')
    filt_label = tk.Label(content, text='Атрибут, по которому будет отбор')
    val_label = tk.Label(content, text='Условие')

    df_entry = ttk.Entry(content, textvariable=df, width=45)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)
    filt_entry = ttk.Entry(content, textvariable=filt, width=45)
    val_entry = ttk.Entry(content, textvariable=val, width=45)

    button = tk.Button(content, text='Вывести', command=lambda: create_otchet_window(rt,
                                                                                     back_names_cond(attr_entry.get(),
                                                                                                     filt_entry.get(),
                                                                                                     val_entry.get())))

    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_entry.grid(column=1, row=1)
    attr_label.grid(column=0, row=2)
    attr_entry.grid(column=1, row=2)
    filt_label.grid(column=0, row=3)
    filt_entry.grid(column=1, row=3)
    val_label.grid(column=0, row=4)
    val_entry.grid(column=1, row=4)
    button.grid(column=0, row=5)
    xs.grid(column=0, row=9, sticky='we', columnspan=3)
    ys.grid(column=3, row=6, sticky='ns', rowspan=3)
    t.grid(column=0, row=6, sticky='nwes', columnspan=3, rowspan=3)
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(0, weight=1)


def many_attr_search_filter(rt, content):
    """
    Создание окна для поиска по нескольким атрибутам и условиям
    """

    for widget in content.winfo_children():
        widget.destroy()

    t = tk.Text(content, width=70, height=30)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set
    t.insert(1.0, 'Здесь будет выводится текст отчета')

    df = tk.StringVar()
    attr = tk.StringVar()
    filt = tk.StringVar()
    val = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибуты (писать через запятую)')
    filt_label = tk.Label(content, text='Атрибуты, по которым будет отбор')
    val_label = tk.Label(content, text='Условия')

    df_entry = ttk.Entry(content, textvariable=df, width=45)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)
    filt_entry = ttk.Entry(content, textvariable=filt, width=45)
    val_entry = ttk.Entry(content, textvariable=val, width=45)

    button = tk.Button(content, text='Вывести', command=lambda: create_otchet_window(rt,
                                                                                     back_many_cond(attr_entry.get(),
                                                                                                    filt_entry.get(),
                                                                                                    val_entry.get())))
    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_entry.grid(column=1, row=1)
    attr_label.grid(column=0, row=2)
    attr_entry.grid(column=1, row=2)
    filt_label.grid(column=0, row=3)
    filt_entry.grid(column=1, row=3)
    val_label.grid(column=0, row=4)
    val_entry.grid(column=1, row=4)
    button.grid(column=0, row=5)
    xs.grid(column=0, row=9, sticky='we', columnspan=3)
    ys.grid(column=3, row=6, sticky='ns', rowspan=3)
    t.grid(column=0, row=6, sticky='nwes', columnspan=3, rowspan=3)
    content.grid_columnconfigure(0, weight=1)
    content.grid_rowconfigure(0, weight=1)


def create_otchet_window(root, df):
    """
    ATTENTION Это код полякова не ебу че тут творится
    Создание окна текстового отчета
    """
    height = df.shape[0]
    try:
        width = df.shape[1]
    except:
        width = 1
    # Массив указателей на виджеты Entry
    pnt = np.empty(shape=(height, width), dtype="O")
    # Массив указателей на текстовые буферы для передачи данных
    vrs = np.empty(shape=(height, width), dtype="O")

    # До любык обращений к tkinter, посокльку запускает интерпретатор
    root = tk.Toplevel(root)

    # Инициализация указателей на буферы
    for i in range(height):
        for j in range(width):
            vrs[i, j] = tk.StringVar()
    # Построение таблицы
    # Структура окна
    top = tk.LabelFrame(root, text="Справочник")
    top.pack(side=tk.TOP)
    # Заполнение значений
    for i in range(height):
        for j in range(width):
            pnt[i, j] = tk.Entry(top, textvariable=vrs[i, j])
            pnt[i, j].grid(row=i, column=j)
    # Заполнение таблицы значениями
    for i in range(height):
        for j in range(width):
            try:
                cnt = df.iloc[i, j]
            except:
                cnt = df.iloc[i]
            vrs[i, j].set(str(cnt))
