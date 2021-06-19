# -*- coding: utf-8 -*-
"""
Главный скрипт.
Задействует все модули программы.
"""

# import os
# import sys
import tkinter as tk
from tkinter import ttk
from coms import load, end
from windows_creating import add_row,\
    one_attr_search,\
    many_attr_search,\
    one_attr_search_filter,\
    many_attr_search_filter

rt = tk.Tk()
rt.geometry('600x600')

fr = ttk.Frame(rt)

# Меню
mainmenu = tk.Menu(rt, tearoff=0)

file = tk.Menu(mainmenu, tearoff=0)
file.add_command(label='Открыть файл', command=load)
file.add_command(label='Добавить запись', command=lambda: add_row(rt, fr))
file.add_command(label='Завершить работу', command=lambda: end(rt))

text_report = tk.Menu(mainmenu, tearoff=0)
text_report.add_command(label='Отчет по одному атрибуту', command=lambda: one_attr_search(rt, fr))
text_report.add_command(label='Отчет по одному атрибуту с фильтром', command=lambda: one_attr_search_filter(rt, fr))
text_report.add_command(label='Отчет по двум атрибутам', command=lambda: many_attr_search(rt, fr))
text_report.add_command(label='Отчет по двум атрибутам с фильтром', command=lambda: many_attr_search_filter(rt, fr))

graf_report = tk.Menu(mainmenu, tearoff=0)
graf_report.add_command(label='Гистограмма')
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
