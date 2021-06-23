# -*- coding: utf-8 -*-
"""
Скрипт, содержащий функции для создания окон и работы с ними
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_interaction import adding_to_workers, adding_to_children, adding_to_otdeli, deleting, \
    save, back_attr, back_named_col, back_names_cond, back_many_cond, \
    get_workers, get_children, get_deps
from plotting import make_plot


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
    add = tk.Button(content, text='Добавить запись', width=20,
                    command=lambda: adding_to_workers(fio_entry.get(), birth_entry.get(), child_entry.get(),
                    vac_entry.get(), dep_entry.get(), prof_entry.get(), pay_entry.get()))
    df = get_workers()

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
    attr_list = [fio_entry.get(), birth_entry.get(), garden_entry.get()]
    add = tk.Button(content, text='Добавить запись', width=20,
                    command=lambda: adding_to_children(fio_entry.get(),
                                                       birth_entry.get(),
                                                       garden_entry.get()))
    df = get_children()
    print(df.loc[df.isin(['a','01.01.2001',1]).any(axis=1)].index.tolist())

    content.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=3)
    fio_label.grid(column=0, row=1)
    birth_label.grid(column=0, row=2)
    garden_label.grid(column=0, row=3)
    fio_entry.grid(column=3, row=1, columnspan=2)
    birth_entry.grid(column=3, row=2, columnspan=2)
    garden_entry.grid(column=3, row=3, columnspan=2)
    add.grid(column=3, row=9, columnspan=2)

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
    add = tk.Button(content, text='Добавить запись', width=20,
                    command=lambda: adding_to_otdeli(num_entry.get(), date_entry.get(),
                                                     tel_entry.get(), num_workers_entry.get()))

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


def one_attr_search(rt, content):
    """
    Создание окна для поиска по одному атрибуту
    """

    for widget in content.winfo_children():
        widget.destroy()

    t = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    attr = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по одному атрибуту')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибут')
    df_combobox = ttk.Combobox(content, values=['Работники', 'Дети работников', 'Отделы'], width=50)
    attr_entry = ttk.Entry(content, textvariable=attr, width=50)
    button = tk.Button(content, text='Вывести',
                       command=lambda: create_otchet_window(rt, t, back_attr(df_combobox.get(),
                                                                             attr_entry.get())))

    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_combobox.grid(column=1, row=1)
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

    t = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    attr = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибуты писать через запятую')

    df_combobox = ttk.Combobox(content, values=['Работники', 'Дети работников', 'Отделы'], width=50)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)

    button = tk.Button(content, text='Вывести',
                       command=lambda: create_otchet_window(rt, t, back_named_col(df_combobox.get(),
                                                                                  attr_entry.get())))

    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_combobox.grid(column=1, row=1)
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

    t = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    attr = tk.StringVar()
    filt = tk.StringVar()
    val = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибут')
    filt_label = tk.Label(content, text='Атрибут, по которому будет отбор')
    val_label = tk.Label(content, text='Условие')

    df_combobox = ttk.Combobox(content, values=['Работники', 'Дети работников', 'Отделы'], width=50)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)
    filt_entry = ttk.Entry(content, textvariable=filt, width=45)
    val_entry = ttk.Entry(content, textvariable=val, width=45)

    button = tk.Button(content, text='Вывести',
                       command=lambda: create_otchet_window(rt, t, back_names_cond(df_combobox.get(),
                                                                                   attr_entry.get(),
                                                                                   filt_entry.get(),
                                                                                   val_entry.get())))

    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_combobox.grid(column=1, row=1)
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

    t = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=t.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=t.xview)
    t['yscrollcommand'] = ys.set
    t['xscrollcommand'] = xs.set

    attr = tk.StringVar()
    filt = tk.StringVar()
    val = tk.StringVar()

    label = tk.Label(content, text='Вывод текстового отчета по нескольким атрибутам')
    df_label = tk.Label(content, text='Справочник')
    attr_label = tk.Label(content, text='Атрибуты (писать через запятую)')
    filt_label = tk.Label(content, text='Атрибуты, по которым будет отбор')
    val_label = tk.Label(content, text='Условия')

    df_combobox = ttk.Combobox(content, values=['Работники', 'Дети работников', 'Отделы'], width=50)
    attr_entry = ttk.Entry(content, textvariable=attr, width=45)
    filt_entry = ttk.Entry(content, textvariable=filt, width=45)
    val_entry = ttk.Entry(content, textvariable=val, width=45)

    button = tk.Button(content, text='Вывести',
                       command=lambda: create_otchet_window(rt, t, back_many_cond(df_combobox.get(),
                                                                                  attr_entry.get(),
                                                                                  filt_entry.get(),
                                                                                  val_entry.get())))
    content.grid(column=0, row=0, columnspan=3, rowspan=8)
    label.grid(column=0, row=0)
    df_label.grid(column=0, row=1)
    df_combobox.grid(column=1, row=1)
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


def back_graph_rep(rt, content):
    """
    Функция для составления графических отчетов
    :param rt:
    :param content:
    :return:
    """
    def on_click():
        """
        Подфункция для считывания значения combobox
        :return:
        """
        global reports
        dict_type = dict_combobox.get()
        graph_type = graph_combobox.get()
        if dict_type == 'Работники':
            if graph_type == 'Гистограмма':
                reports = ['Гистограмма распределения рабочих по годам рождения',
                           'Гистограмма распределения зарплат рабочих']
            elif graph_type == 'Диаграмма рассеивания':
                reports = ['Рассеянная диаграмма зарплат работников по возрасту']
            elif graph_type == 'Столбчатая диаграмма':
                reports = ['Столбчатая диаграмма средней зп по отделам',
                           'Столбчатая диаграмма вакцинированных и невакцинированных от COVID-19']
        elif dict_type == 'Дети работников':
            if graph_type == 'Гистограмма':
                reports = ['Гистограмма распределения детей по годам рождения']
            elif graph_type == 'Столбчатая диаграмма':
                reports = ['Столбчатая диаграмма распределения детей по садикам']
        elif dict_type == 'Отделы':
            if graph_type == 'Столбчатая диаграмма':
                reports = ['Столбчатая диаграмма распределения сотрудников по отделам']
        try:
            rep_combobox.configure(values=reports)
        except NameError:
            messagebox.showerror("Error", "Вызываемого атрибута не существует")

    for widget in content.winfo_children():
        widget.destroy()

    reports = []

    dict_label = tk.Label(content, text='Выберите словарь', width=50)
    graph_label = tk.Label(content, text='Выберите тип графика', width=50)
    rep_label = tk.Label(content, text='Выберите графический отчет', width=50)
    dict_combobox = ttk.Combobox(content, values=['Работники', 'Дети работников',
                                                  'Отделы'], width=50)
    graph_combobox = ttk.Combobox(content, values=['Гистограмма', 'Диаграмма рассеивания',
                                                   'Столбчатая диаграмма'], width=50)
    button_1 = tk.Button(content, text='Показать доступные отчеты', command=on_click)
    rep_combobox = ttk.Combobox(content, values=reports, width=50)
    button_2 = tk.Button(content, text='Вывести',
                         command=lambda: make_plot(dict_combobox.get(), graph_combobox.get(),
                                                   rep_combobox.get()))

    content.grid(column=0, row=0)
    dict_label.grid(column=0, row=0)
    dict_combobox.grid(column=1, row=0)
    graph_label.grid(column=0, row=1)
    graph_combobox.grid(column=1, row=1)
    button_1.grid(column=1, row=2)
    rep_label.grid(column=0, row=3)
    rep_combobox.grid(column=1, row=3)
    button_2.grid(column=1, row=4)


def show_dict_workers(rt, content):
    """
    Функция для работы со словарями справочника workers
    :param rt:
    :param content:
    :return:
    """
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Нормализованный словарь рабочих', width=50)
    text = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=text.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=text.xview)
    text['yscrollcommand'] = ys.set
    text['xscrollcommand'] = xs.set

    content.grid(column=0, row=0)
    label.grid(column=0, row=0)
    xs.grid(column=0, row=2, sticky='we')
    ys.grid(column=1, row=1, sticky='ns')
    text.grid(column=0, row=1, sticky='nwes')
    text.insert(1.0, get_workers().to_string())


def show_dict_children(rt, content):
    """
    Функция для работы со словарями справочника children
    :param rt:
    :param content:
    :return:
    """
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Нормализованный словарь детей рабочих', width=50)
    text = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=text.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=text.xview)
    text['yscrollcommand'] = ys.set
    text['xscrollcommand'] = xs.set

    content.grid(column=0, row=0)
    label.grid(column=0, row=0)
    xs.grid(column=0, row=2, sticky='we')
    ys.grid(column=1, row=1, sticky='ns')
    text.grid(column=0, row=1, sticky='nwes')
    text.insert(1.0, get_children().to_string())


def show_dict_deps(rt, content):
    """
    Функция для работы со словарями справочника otdeli
    :param rt:
    :param content:
    :return:
    """
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Нормализованный словарь отделов', width=50)
    text = tk.Text(content, width=120, height=30, wrap=tk.NONE)
    ys = ttk.Scrollbar(content, orient='vertical', command=text.yview)
    xs = ttk.Scrollbar(content, orient='horizontal', command=text.xview)
    text['yscrollcommand'] = ys.set
    text['xscrollcommand'] = xs.set

    content.grid(column=0, row=0)
    label.grid(column=0, row=0)
    xs.grid(column=0, row=2, sticky='we')
    ys.grid(column=1, row=1, sticky='ns')
    text.grid(column=0, row=1, sticky='nwes')
    text.insert(1.0, get_deps().to_string())


def create_otchet_window(root, text, df):
    """
    Создание окна текстового отчета
    """
    try:
        text.delete(1.0, tk.END)
        text.insert(1.0, df.to_string())
    except AttributeError:
        messagebox.showerror("Error", "Вызов несуществующего атрибута")

def change_row(rt, content, db_name):
    for widget in content.winfo_children():
        widget.destroy()

    label = tk.Label(content, text='Редактирование и удаление записей')
    num_label = tk.Label(content, text='Введите индекс:')
    index_entry = ttk.Entry(content, width=40)
    add = tk.Button(content, text='Получить запись', width=20)
    content.grid(column=0, row=0)
    label.grid(column=0, row=0)
    num_label.grid(column=0, row=1)
    index_entry.grid(column=2, row=1)
    add.grid(column=3, row=1)