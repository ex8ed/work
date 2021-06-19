# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:48:12 2021

@author: khusn
"""

import os
import sys
import tkinter as tk
from tkinter import ttk

os.chdir("C:/Users/Nick/Documents/work/")
sys.path.append("С:/Users/Nick/Documents/work/")

rt = tk.Tk()
rt.geometry('800x400')

# Меню
mainmenu = tk.Menu(rt, tearoff=0)

file = tk.Menu(mainmenu, tearoff=0)
file.add_command(label='Открыть файл')
file.add_command(label='Изменить файл')
file.add_command(label='Завершить работу')

text_report = tk.Menu(mainmenu, tearoff=0)
text_report.add_command(label='Отчет по одному атрибуту')
text_report.add_command(label='Отчет по одному атрибуту с фильтром')
text_report.add_command(label='Отчет по двум атрибутам')
text_report.add_command(label='Отчет по двум атрибутам с фильтром')

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
