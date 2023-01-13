from input_data import input_data
from init import init_del
from write_data import write_data



def push_data():
    dct = input_data()

    # id;surname;name;class;status   - name.csv
    write_data([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("class"), dct.get("status")], "name.csv")

    # id;city;street;house;apartament;other  - class.csv
    write_data([dct["id"], dct["city"], dct["street"], dct["house"], dct["apartament"], dct["other"]], "adress.csv")

    # id;row;col;room - adress.csv
    write_data([dct["id"], dct["row"], dct["col"], dct["room"]], "class.csv")
    
    # id;row;fio;predmet - teacher.csv
    write_data([dct["id"], dct["fio"], dct["predmet"]], "teacher.csv")
    
def push_data_change(data):
    
    init_del()
    
    for item in data:
      
        # id;surname();name;class;status   - name.csv
        write_data([item[0], item[1], item[2], item[3],item[4]], "name.csv")

         # id;city;street;house;apartament;other  - class.csv
        write_data([item[0], item[8], item[9], item[10], item[11], item[12]], "adress.csv")

        # id;row;col;room - adress.csv
        write_data([item[0], item[5], item[6], item[7]], "class.csv")
    
         # id;row;fio;predmet - teacher.csv
        write_data([item[0], item[13], item[14]], "teacher.csv")