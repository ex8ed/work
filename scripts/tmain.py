# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:48:12 2021

@author: khusn
"""

#import os
#import sys
import tkinter as tk
from tkinter import ttk
from coms import load, end
from windows_creating import add_workers_row, add_children_row, add_otdeli_row, one_attr_search, many_attr_search, one_attr_search_filter, many_attr_search_filter, back_hist_rep

rt = tk.Tk()
rt.geometry('1000x800')

fr = ttk.Frame(rt)

# Меню
mainmenu = tk.Menu(rt, tearoff=0)

add_row = tk.Menu(mainmenu, tearoff=0)
add_row.add_command(label='Добавить запись в справочник Workers', command=lambda: add_workers_row(rt, fr))
add_row.add_command(label='Добавить запись в справочник Children', command=lambda: add_children_row(rt, fr))
add_row.add_command(label='Добавить запись в справочник Otdeli', command=lambda: add_otdeli_row(rt, fr))

file = tk.Menu(mainmenu, tearoff=0)
file.add_command(label='Открыть файл', command=load)
file.add_cascade(label='Добавить запись', menu=add_row)
file.add_command(label='Завершить работу', command=lambda: end(rt, fr))

text_report = tk.Menu(mainmenu, tearoff=0)
text_report.add_command(label='Отчет по одному атрибуту', command = lambda: one_attr_search(rt, fr))
text_report.add_command(label='Отчет по одному атрибуту с фильтром', command = lambda: one_attr_search_filter(rt, fr))
text_report.add_command(label='Отчет по двум атрибутам', command = lambda: many_attr_search(rt, fr))
text_report.add_command(label='Отчет по двум атрибутам с фильтром', command = lambda: many_attr_search_filter(rt, fr))

graf_report = tk.Menu(mainmenu, tearoff=0)
graf_report.add_command(label='Гистограмма', command = lambda: back_hist_rep(rt, fr))
graf_report.add_command(label='Диаграмма Бокса-Уискера')
graf_report.add_command(label='Диаграмма рассеивания')
graf_report.add_command(label='Столбчатая диаграмма')

cfg = tk.Menu(mainmenu, tearoff=0)

help_menu = tk.Menu(mainmenu, tearoff=0)
help_menu.add_command(label='Руководство пользователя')
help_menu.add_command(label='О приложении')

mainmenu.add_cascade(label='Файл', menu=file)
mainmenu.add_cascade(label='Текстовые отчеты', menu=text_report)
mainmenu.add_cascade(label='Графические отчеты', menu=graf_report)
mainmenu.add_cascade(label='Настройки', menu=cfg)
mainmenu.add_cascade(label='Помощь', menu=help_menu)

rt.config(menu=mainmenu)

rt.mainloop()
