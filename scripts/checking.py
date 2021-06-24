# -*- coding: utf-8 -*-
"""Storing Validation-checking functions"""


def chars(string):
    if ''.join([x.strip() for x in string.replace('.', ' ').split()]).isalpha():
        return string
    return False


def numerical(string):
    if string.strip().isdigit():
        return string
    return False


def phone_number(number):
    """
        Функция проверяет корректность
        введенного в справочник номера телефона
    :param number: данный номер телефона
    :return: Логическая константа-ответ.
    """
    if len(number) >= 12:
        E_G = number[1:].replace('-', '')
        try:
            int(E_G)
            return True
        except ValueError:
            print("Unuseful number format")
            return False
    else:
        return False


def data(data_str):
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
