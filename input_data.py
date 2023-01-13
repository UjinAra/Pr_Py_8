from write_data import count_data



def input_data():
    dct = dict()
    Id = count_data("name.csv") 
    dct["id"] = Id     # list[0] - это Id ученика
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["status"] = input('Введите Успеваемость: ')
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    dct["room"] = input('Введите Номер кабинета: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    dct["fio"] = input('Введите Фио Классного руководителя: ')
    dct["predmet"] = input('Введите Предмет Классного Руководителя: ')

    return dct


     