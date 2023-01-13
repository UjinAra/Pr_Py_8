import os

def os_file (file):
    return os.path.exists(file)

def init():
    if os_file("name.csv") == False:
        with open("name.csv", 'a+') as file:
            file.write("id;surname;name;class;status\n")
            
    if os_file("adress.csv") == False:
        with open("adress.csv", 'a+') as file:
            file.write("id;city;street;house;apartament;other\n")
            
    if os_file("class.csv") == False:
        with open("class.csv", 'a+') as file:
            file.write("id;row;col;room\n")
    
    if os_file("teacher.csv") == False:
       with open("teacher.csv", 'a+') as file:
            file.write("id;fio;predmet\n")
            
def init_del():

    with open("name.csv", 'w') as file:
        file.write("id;surname;name;class;status\n")
            
    with open("adress.csv", 'w') as file:
        file.write("id;city;street;house;apartament;other\n")
            
    with open("class.csv", 'w') as file:
        file.write("id;row;col;room\n")
    
    with open("teacher.csv", 'w') as file:
        file.write("id;fio;predmet\n")