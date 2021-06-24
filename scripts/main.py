# -*- coding: utf-8 -*-
"""
Главный скрипт приложения
"""
import os
import tkinter as tk
from tkinter import ttk
from db_interaction import end, load_default_text
from windows_creating import add_workers_row, add_children_row, \
    add_otdeli_row, one_attr_search, many_attr_search, one_attr_search_filter, \
    many_attr_search_filter, back_graph_rep, show_dict_workers, \
    show_dict_children, show_dict_deps, change_row, show_info, show_help


# объявление рабочей директории
PTH = os.getcwd()
os.chdir(PTH[:len(PTH) - 8])
rt = tk.Tk()
rt.geometry('980x600')
rt.resizable(False, False)

fr = ttk.Frame(rt)

text = tk.Text(fr, width=120, height=30, wrap=tk.NONE)
text.insert(1.0, load_default_text())

fr.grid(column=0, row=0)
text.grid(column=0, row=0)

# Меню
main_menu = tk.Menu(rt, tearoff=0)


add_row = tk.Menu(main_menu, tearoff=0)
add_row.add_command(label='Добавить запись в справочник Workers',
                    command=lambda: add_workers_row(fr))
add_row.add_command(label='Добавить запись в справочник Children',
                    command=lambda: add_children_row(fr))
add_row.add_command(label='Добавить запись в справочник Otdeli',
                    command=lambda: add_otdeli_row(fr))


changing_row = tk.Menu(main_menu, tearoff=0)
changing_row.add_command(label='Изменить или удалить запись в справочнике Workers',
                         command=lambda: change_row(fr, 'Работники'))
changing_row.add_command(label='Изменить или удалить запись в справочнике Children',
                         command=lambda: change_row(fr, 'Дети работников'))
changing_row.add_command(label='Изменить или удалить запись в справочнике Otdeli',
                         command=lambda: change_row(fr, 'Отделы'))


show_dict = tk.Menu(main_menu, tearoff=0)
show_dict.add_command(label='Словарь рабочих', command=lambda: show_dict_workers(fr))
show_dict.add_command(label='Словарь детей рабочих', command=lambda: show_dict_children(fr))
show_dict.add_command(label='Словарь отделений', command=lambda: show_dict_deps(fr))


# Создание каскада для пункта меню "Нормализованные словари"
show_dict = tk.Menu(main_menu, tearoff=0)
show_dict.add_command(label='Словарь рабочих', command=lambda: show_dict_workers(fr))
show_dict.add_command(label='Словарь детей рабочих', command=lambda: show_dict_children(fr))
show_dict.add_command(label='Словарь отделений', command=lambda: show_dict_deps(fr))


# Создание каскада для пункта меню "Нормализованные словари"
show_dict = tk.Menu(main_menu, tearoff=0)
show_dict.add_command(label='Словарь рабочих', command=lambda: show_dict_workers(fr))
show_dict.add_command(label='Словарь детей рабочих', command=lambda: show_dict_children(fr))
show_dict.add_command(label='Словарь отделений', command=lambda: show_dict_deps(fr))


# Создание пункта меню "Файл"
file = tk.Menu(main_menu, tearoff=0)
file.add_cascade(label='Нормализованные словари', menu=show_dict)
file.add_cascade(label='Добавить запись', menu=add_row)
file.add_cascade(label='Изменить или удалить запись', menu=changing_row)
file.add_command(label='Завершить работу', command=lambda: end(rt))


# Создание пункта меню "Текстовые отчеты"
text_report = tk.Menu(main_menu, tearoff=0)
text_report.add_command(label='Отчет по одному атрибуту', command=lambda: one_attr_search(fr))
text_report.add_command(label='Отчет по множеству атрибутов по одному ключу',
                        command=lambda: one_attr_search_filter(fr))
text_report.add_command(label='Отчет по множеству атрибутов', command=lambda: many_attr_search(fr))
text_report.add_command(label='Отчет по множеству атрибутов по двум ключам',
                        command=lambda: many_attr_search_filter(fr))


help_menu = tk.Menu(main_menu, tearoff=0)
help_menu.add_command(label='Руководство пользователя')
help_menu.add_command(label='О приложении')


# Создание пункта меню "Помощь"
help_menu = tk.Menu(main_menu, tearoff=0)
help_menu.add_command(label='Руководство пользователя', command=lambda: show_help(fr))
help_menu.add_command(label='О приложении', command=lambda: show_info(fr))


# Создание пункта меню "Помощь"
help_menu = tk.Menu(main_menu, tearoff=0)
help_menu.add_command(label='Руководство пользователя', command=lambda: show_help(fr))
help_menu.add_command(label='О приложении', command=lambda: show_info(fr))


# Создание меню приложения
main_menu.add_cascade(label='Файл', menu=file)
main_menu.add_cascade(label='Текстовые отчеты', menu=text_report)
main_menu.add_command(label='Графические отчеты', command=lambda: back_graph_rep(fr))
main_menu.add_cascade(label='Помощь', menu=help_menu)


rt.config(menu=main_menu)

rt.mainloop()
