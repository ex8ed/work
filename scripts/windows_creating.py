# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:48:12 2021

@author: khusn
"""

import tkinter as tk
import numpy as np
from tkinter import ttk
from coms import adding_to_workers, adding_to_children, adding_to_otdeli, deleting, back_attr,back_named_col,  back_names_cond, back_many_cond, back_columns, back_value_columns

def add_workers_row(rt, content):
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
    add = tk.Button(content, text='Добавить запись', width=20, command = lambda:adding_to_workers(
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
    
def add_children_row(rt, content):
    """
    Создание окна для добавления записи в исходную базу данных
    """
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Добавление, редактирование и удаление записей')
    fio_label = tk.Label(content, text='ФИО ребенка')
    birth_label = tk.Label(content, text='Дата рождения')
    garden_label = tk.Label(content, text='Номер садика')
    fio_entry = ttk.Entry(content, width=40)
    birth_entry = ttk.Entry(content, width=40)
    garden_entry = ttk.Entry(content, width=40)
    add = tk.Button(content, text='Добавить запись', width=20, command = lambda:adding_to_children(
        fio_entry.get(), birth_entry.get(), garden_entry.get()))
    update = tk.Button(content, text='Обновить запись', width=20)
    delete = tk.Button(content, text='Удалить запись', width=20, command=deleting)

    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    fio_label.grid(column=0, row=1)
    birth_label.grid(column=0, row=2)
    garden_label.grid(column=0, row=3)
    fio_entry.grid(column=3, row=1, columnspan=2)
    birth_entry.grid(column=3, row=2, columnspan=2)
    garden_entry.grid(column=3, row=3, columnspan=2)
    add.grid(column=3, row=9, columnspan=2)
    update.grid(column=3, row=10, columnspan=2)
    delete.grid(column=3, row=11, columnspan=2)
    
def add_otdeli_row(rt, content):
    """
    Создание окна для добавления записи в исходную базу данных
    """
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Добавление, редактирование и удаление записей')
    num_label = tk.Label(content, text='Номер отдела')
    date_label = tk.Label(content, text='Дата создания')
    tel_label = tk.Label(content, text='Телефон')
    num_workers_label = tk.Label(content, text='Количество сотрудников')
    num_entry = ttk.Entry(content, width=40)
    date_entry = ttk.Entry(content, width=40)
    tel_entry = ttk.Entry(content, width=40)
    num_workers_entry = ttk.Entry(content, width=40)
    add = tk.Button(content, text='Добавить запись', width=20, command = lambda:adding_to_otdeli(
        num_entry.get(), date_entry.get(), tel_entry.get(), num_workers_entry.get(),))
    update = tk.Button(content, text='Обновить запись', width=20)
    delete = tk.Button(content, text='Удалить запись', width=20, command=deleting)

    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    num_label.grid(column=0, row=1)
    date_label.grid(column=0, row=2)
    tel_label.grid(column=0, row=3)
    num_workers_label.grid(column=0, row=4)
    num_entry.grid(column=3, row=1, columnspan=2)
    date_entry.grid(column=3, row=2, columnspan=2)
    tel_entry.grid(column=3, row=3, columnspan=2)
    num_workers_entry.grid(column=3, row=4, columnspan=2)
    add.grid(column=3, row=9, columnspan=2)
    update.grid(column=3, row=10, columnspan=2)
    delete.grid(column=3, row=11, columnspan=2)

def one_attr_search(rt, content):
    """
    Создание окна для поиска по одному атрибуту
    """
    
    for widget in content.winfo_children():
        widget.destroy()

    t = tk.Text(content, width=100, height=30)
    ys = ttk.Scrollbar(content, orient = 'vertical', command = t.yview)
    xs = ttk.Scrollbar(content, orient = 'horizontal', command = t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    df = tk.StringVar()
    attr = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по одному атрибуту')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибут')

    df_entry = ttk.Entry(content, textvariable=df, width=45)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)

    button = tk.Button(content, text='Вывести', command=lambda: create_otchet_window(rt, t, back_attr(attr_entry.get())))

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

    t = tk.Text(content, width=100, height=30)
    ys = ttk.Scrollbar(content, orient = 'vertical', command = t.yview)
    xs = ttk.Scrollbar(content, orient = 'horizontal', command = t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    df = tk.StringVar()
    attr = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибуты писать через запятую')

    df_entry = ttk.Entry(content, textvariable=df, width=45)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)

    button = tk.Button(content, text='Вывести', command =lambda: create_otchet_window(rt, t, back_named_col(attr_entry.get())))

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

    t = tk.Text(content, width=100, height=30)
    ys = ttk.Scrollbar(content, orient = 'vertical', command = t.yview)
    xs = ttk.Scrollbar(content, orient = 'horizontal', command = t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    df = tk.StringVar()
    attr = tk.StringVar()
    filt = tk.StringVar()
    val = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибут')
    filt_label = tk.Label(content, text='Атрибут, по которому будет отбор')
    val_label = tk.Label(content, text='Условие')

    df_entry = ttk.Entry(content, textvariable=df, width=45)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)
    filt_entry = ttk.Entry(content, textvariable=filt, width=45)
    val_entry = ttk.Entry(content, textvariable=val, width=45)

    button = tk.Button(content, text='Вывести', command =lambda: create_otchet_window(rt, t, back_names_cond(attr_entry.get(), filt_entry.get(), val_entry.get())))

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

    t = tk.Text(content, width=100, height=30)
    ys = ttk.Scrollbar(content, orient = 'vertical', command = t.yview)
    xs = ttk.Scrollbar(content, orient = 'horizontal', command = t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

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

    button = tk.Button(content, text='Вывести', command =lambda: create_otchet_window(rt, t, back_many_cond(attr_entry.get(), filt_entry.get(), val_entry.get())))
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
    
def back_hist_rep(rt, content):
    
    for widget in content.winfo_children():
        widget.destroy()
        
    label = tk.Label(content, text='Выберите два атрибута для построения гистограммы', width=50)
    name_attr_combobox = ttk.Combobox(content, values=back_columns(), width=50)
    button = tk.Button(content, text='Вывести')
    
    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    name_attr_combobox.grid(column=4, row=0)
    button.grid(column=4, row=2)
    
def back_boxplot_rep(rt, content):
    for widget in content.winfo_children():
        widget.destroy()
        
    label = tk.Label(content, text='Выберите два атрибута для построения диаграммы Бокса-Уискера', width=50)
    name_attr_combobox = ttk.Combobox(content, values=back_columns(), width=50)
    value_attr_combobox = ttk.Combobox(content, values=back_value_columns(), width=50)
    button = tk.Button(content, text='Вывести')
    
    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    name_attr_combobox.grid(column=4, row=0)
    value_attr_combobox.grid(column=4, row=1)
    button.grid(column=4, row=2)
    
def back_spread_rep(rt, content):
    for widget in content.winfo_children():
        widget.destroy()
        
    label = tk.Label(content, text='Выберите два атрибута для построения диаграммы рассеивания', width=50)
    name_attr_combobox = ttk.Combobox(content, values=back_columns(), width=50)
    value_attr_combobox = ttk.Combobox(content, values=back_value_columns(), width=50)
    button = tk.Button(content, text='Вывести')
    
    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    name_attr_combobox.grid(column=4, row=0)
    value_attr_combobox.grid(column=4, row=1)
    button.grid(column=4, row=2)
    
def back_columns_rep(rt, content):
    for widget in content.winfo_children():
        widget.destroy()
        
    label = tk.Label(content, text='Выберите два атрибута для построения стобчатой диаграммы', width=50)
    name_attr_combobox = ttk.Combobox(content, values=back_columns(), width=50)
    value_attr_combobox = ttk.Combobox(content, values=back_value_columns(), width=50)
    button = tk.Button(content, text='Вывести')
    
    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    name_attr_combobox.grid(column=4, row=0)
    value_attr_combobox.grid(column=4, row=1)
    button.grid(column=4, row=2)
    
  
def back_graph_rep(rt, content):
    def on_click():
        global reports
        graph_type = graph_combobox.get()
        print(graph_type == 'Гистограмма')
        if graph_type == 'Гистограмма':
            reports = ['1', '2', '3']
        elif graph_type == 'Диаграмма Бокса-Уискера':
            reports = ['1', '2']
        elif graph_type == 'Диаграмма рассеивания':
            reports = ['1']
        elif graph_type == 'Столбчатая диаграмма':
            reports = ['1', '2', '3', '4']
        rep_combobox.configure(values=reports)
        
    for widget in content.winfo_children():
        widget.destroy()
    
    reports = []
    
    dict_label = tk.Label(content, text='Выберите словарь', width=50)
    graph_label = tk.Label(content, text='Выберите тип графика', width=50)
    rep_label = tk.Label(content, text='Выберите графический отчет', width=50)
    dict_combobox = ttk.Combobox(content, values=['Работники', 'Дети работников', 'Отделы'], width=50)
    graph_combobox = ttk.Combobox(content, values=['Гистограмма', 'Диаграмма Бокса-Уискера', 'Диаграмма рассеивания', 'Столбчатая диаграмма'], width=50)
    button_1 = tk.Button(content, text='Подтвердить', command=on_click)
    rep_combobox = ttk.Combobox(content, values=reports, width=50)
    button_2 = tk.Button(content, text='Вывести')
    
    content.grid(column=0, row=0)
    dict_label.grid(column=0, row=0)
    dict_combobox.grid(column=1, row=0)
    graph_label.grid(column=0, row=1)
    graph_combobox.grid(column=1, row=1)
    button_1.grid(column=1, row=2)
    rep_label.grid(column=0, row=3)
    rep_combobox.grid(column=1, row=3)
    button_2.grid(column=1, row=4)
    
    
def create_otchet_window(root, text, df):
    """
    ATTENTION Это код полякова не ебу че тут твориться
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

    # Инициализация указателей на буферы
    # for i in range(height):
    #     for j in range(width):
    #         vrs[i, j] = tk.StringVar()
            
    # Построение таблицы
    # Структура окна
    # top = tk.LabelFrame(frame, text="Справочник")
    # top.grid(column=0, row=0)
    # # Заполнение значений
    # for i in range(height):
    #     for j in range(width):
    #         pnt[i, j] = tk.Entry(top, textvariable=vrs[i, j])
    #         pnt[i, j].grid(row=i, column=j)
    
    # Заполнение таблицы значениями
    # for i in range(height):
    #     for j in range(width):
    #         try:
    #             cnt = df.iloc[i, j]
    #         except:
    #             cnt = df.iloc[i]
    #         vrs[i, j].set(str(cnt))
    
    text.delete(1.0, tk.END)
    text.insert(1.0, df.to_string())
