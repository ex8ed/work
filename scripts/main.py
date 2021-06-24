# -*- coding: utf-8 -*-
"""
Главный скрипт приложения
"""
import os
import tkinter as tk
from tkinter import ttk
from db_interaction import end
from windows_creating import add_workers_row, add_children_row, \
    add_otdeli_row, one_attr_search, many_attr_search, one_attr_search_filter, \
    many_attr_search_filter, back_graph_rep, show_dict_workers, \
    show_dict_children, show_dict_deps, change_row

PTH = os.getcwd()
os.chdir(PTH[:len(PTH) - 8])

rt = tk.Tk()
rt.geometry('1280x720')
rt.resizable(False, False)

fr = ttk.Frame(rt)

# Меню
mainmenu = tk.Menu(rt, tearoff=0)

add_row = tk.Menu(mainmenu, tearoff=0)
add_row.add_command(label='Добавить запись в справочник Workers',
                    command=lambda: add_workers_row(rt, fr))
add_row.add_command(label='Добавить запись в справочник Children',
                    command=lambda: add_children_row(rt, fr))
add_row.add_command(label='Добавить запись в справочник Otdeli',
                    command=lambda: add_otdeli_row(rt, fr))

changing_row = tk.Menu(mainmenu, tearoff=0)
changing_row.add_command(label='Изменить или удалить запись в справочнике Workers',
                    command=lambda: change_row(rt, fr, 'Работники'))
changing_row.add_command(label='Изменить или удалить запись в справочнике Children',
                    command=lambda: change_row(rt, fr, 'Дети работников'))
changing_row.add_command(label='Изменить или удалить запись в справочнике Otdeli',
                    command=lambda: change_row(rt, fr, 'Отделы'))

show_dict = tk.Menu(mainmenu, tearoff=0)
show_dict.add_command(label='Словарь рабочих', command=lambda: show_dict_workers(rt, fr))
show_dict.add_command(label='Словарь детей рабочих', command=lambda: show_dict_children(rt, fr))
show_dict.add_command(label='Словарь отделений', command=lambda: show_dict_deps(rt, fr))

file = tk.Menu(mainmenu, tearoff=0)
file.add_cascade(label='Нормализованные словари', menu=show_dict)
file.add_cascade(label='Добавить запись', menu=add_row)
file.add_cascade(label='Изменить или удалить запись', menu=changing_row)
file.add_command(label='Завершить работу', command=lambda: end(rt))

text_report = tk.Menu(mainmenu, tearoff=0)
text_report.add_command(label='Отчет по одному атрибуту', command=lambda: one_attr_search(rt, fr))
text_report.add_command(label='Отчет по одному атрибуту по одному ключу',
                        command=lambda: one_attr_search_filter(rt, fr))
text_report.add_command(label='Отчет по множеству атрибутов', command=lambda: many_attr_search(rt, fr))
text_report.add_command(label='Отчет по множеству атрибутов по нескольким ключам',
                        command=lambda: many_attr_search_filter(rt, fr))

cfg = tk.Menu(mainmenu, tearoff=0)

help_menu = tk.Menu(mainmenu, tearoff=0)
help_menu.add_command(label='Руководство пользователя')
help_menu.add_command(label='О приложении')

mainmenu.add_cascade(label='Файл', menu=file)
mainmenu.add_cascade(label='Текстовые отчеты', menu=text_report)
mainmenu.add_command(label='Графические отчеты', command=lambda: back_graph_rep(rt, fr))
mainmenu.add_cascade(label='Помощь', menu=help_menu)

rt.config(menu=mainmenu)

rt.mainloop()
