import csv
import datetime

def add_note():
    new_name = input('Придумайте имя, для заметки: ')
    new_text = input('Введите текст заметки: ') 
    dt_now = datetime.datetime.now()
    id = read_ID() +1
    with open("da.csv", mode="a", encoding='utf-8') as w_file:
        file_w = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        #file_w.writerow(["ID", "Дата", "Название", "Текст"])
        file_w.writerow([id, dt_now, new_name, new_text])

def read():
    with open('da.csv', encoding='utf8') as file:  
        #reader = csv.reader(file, delimiter=",")
        #for row in reader:
         #   print(row)
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            if row=='':
                print(row)
                print("Привет")
            
def read_ID():
    with open('da.csv', encoding='utf8') as file:  
        #reader = csv.reader(file, delimiter=",")
        #for row in reader:
         #   print(row)
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            count= count+1
    return count

def poisk():
    with open('da.csv', encoding='utf8') as file:  
        name = input('Введите название заметки: ')
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if name in row:
                print(row)

def delete():

    with open('da.csv', 'w', encoding='utf8') as file: 
        
        name = input('Введите название заметки: ')
        writer = csv.writer(file)
        with open('da.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            lines = list(reader)
            for row in reader:
                if name in row:
                    del row
        writer.writerows(lines)
def Main():
    a = input("ВВедите: а, если хотите добавить, б, посмотреть по названию, в, если просмотреть список, г, если удалить всё: ")
    if (a == "а"):
        add_note()
    if (a=='в'):
        read()
    if (a=='б'):
       poisk() 
    if (a=='г'):
        delete()

Main()
