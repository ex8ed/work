import matplotlib.pyplot as plt
from db_interaction import return_dict


def scatter():
    """
    Рассеянная диаграмма зарплат работников по возрасту
    """
    workers = return_dict('Работники')
    salary = workers['З/П в месяц'].values
    for y, x in enumerate(workers['Дата рождения'].values):
        plt.scatter((2020 - int(str(x).split('-')[0])), salary[y], color='Blue')
    plt.title('Распределение зарплаты по возрастам')
    plt.show()


def bar_covid():
    """
    Столбчатая диаграмма вакцинированных и невакцинированных от COVID-19
    """
    workers = return_dict('Работники')
    vaccinated = workers[workers['Прививка от COVID-19'] == 'Да'].shape[0]
    not_vaccinated = workers[workers['Прививка от COVID-19'] == 'Нет'].shape[0]
    plt.bar(['Да', 'Нет'], [vaccinated, not_vaccinated])
    plt.title('Вакцинация от COVID-19')
    plt.show()


def bar_sadik():
    """
    Столбчатая диаграмма распределения детей по садикам
    """
    children = return_dict('Дети работников')
    children_aggregated = children.groupby('Номер садика').agg({'Дата рождения ребенка': 'count'}).reset_index()
    plt.bar(children_aggregated['Номер садика'], children_aggregated['Дата рождения ребенка'])
    plt.yticks([3, 6, 9, 12, 15, 18, 21])
    plt.title('Распределение детей по садикам')
    plt.show()


def bar_otdel_salary():
    """
    Столбчатая диаграмма средней зп по отделам
    """
    workers = return_dict('Работники')
    workers_aggregated = workers.groupby('Номер отдела').agg({'З/П в месяц': 'mean'}).reset_index()
    plt.bar(workers_aggregated['Номер отдела'], workers_aggregated['З/П в месяц'])
    plt.xticks([1, 2, 3])
    plt.title('Средняя зп по отделам')
    plt.show()


def bar_otdeli():
    """
    Столбчатая диаграмма распределения сотрудников по отделам
    """
    otdeli = return_dict('Отделы')
    plt.bar(otdeli['Номер отдела'], otdeli['Количество сотрудников'])
    plt.title('Распределение сотрудников по отделам')
    plt.xticks([1, 2, 3])
    plt.show()


def hist_salary():
    """
    Гистограмма распределения зарплат рабочих
    """
    workers = return_dict('Работники')
    workers['З/П в месяц'].hist()
    plt.title('Распределение зарплат рабочих')
    plt.show()


def hist_birth_workers():
    """
    Гистограмма распределения рабочих по годам рождения
    """
    workers = return_dict('Работники')
    workers['Дата рождения'].hist()
    plt.title('Распределение рабочих по годам рождения')
    plt.show()


def hist_birth_children():
    """
    Гистограмма распределения детей по годам рождения
    """
    children = return_dict('Дети работников')
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
