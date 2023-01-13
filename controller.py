
from push_data import *
from read_data import *
from print_data import *
from search_data import *
from del_data import *


def greeting():
    print("Здравствуйте, Вас приветствует лучшая школа РФ!")
    print("-----------------------------------------------")
    
def start():
    
    print("Что Вас интересует:")
    print("------------------------------------------------\n\
    1 - получить всю информацию о учениках;\n\
    2 - добавить ученика;\n\
    3 - поиск ученика;\n\
    4 - удалить ученика;\n\
    5 - выход.")
    print("------------------------------------------------")
    ch = сhecking_the_number(input("Введите цифру: "))
    while True:
        if ch == 1:
            data = read_data()
            print_data(data)
            start()
        
        elif ch == 2:
            push_data()
            start()
            
        elif ch == 3:
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            start()
            
        elif ch == 4:
            info = input("Введите данные которые надо удалить: ")
            data = read_data()
            item = search_data_del(info, data)
            
            if item != None:
                push_data_change(item)
            else:
                print("Данные не обнаружены")                
            start()
            
        elif ch == 5:
            print("Сеанс окончен, до свидания!")
            break
        
        else:
            print("Введите корректную цифру!")
            start()
            
def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

