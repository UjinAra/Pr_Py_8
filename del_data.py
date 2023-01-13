# модуль Удаления контакта
from print_data import print_data

def search_data_del(word, data):
    
    if len(data) > 0:
        lst_del = []
        lst = []
        for item in data:
            if word in item:
                lst_del.append(item)
            else:
                lst.append(item)
        
        if lst_del == []:
            return None
        else:
            print_data(lst_del)
            
            y_n = input('Введите Да, если хотите удалить: ')
            if y_n != "Да":
                return None
            
            return lst
    else:
        return None
    
