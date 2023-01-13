def print_data(data, search = False):
    if len(data) > 0:
        print("id", "Фамилия",":", "Имя",":", "Класс",":", "Статус",":",\
           "Ряд",":", "Парта",":", "Каб.",":",\
            "Город",":", "Улица",":", "Дом",":", "Кв-ра",":", "Прим.",":",\
            "ФИО Кл рук-ль",":","Предмет")
        print("-"*100)
        if not search:
            del data[0]
        for item in data:
            print(item[0],item[1],":",item[2],":", item[3],":", item[4],":",\
            item[5],":",item[6],":",item[7],":",\
            item[8],":", item[9],":", item[10],":", item[11],":", item[12],":",\
            item[13],":", item[14])
    else:
        print("\n")
        print("*"*110 + "\nСправочник пуст!\n" + "*"*110)
        print("\n")