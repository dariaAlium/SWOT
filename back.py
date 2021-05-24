import sqlite3
import matplotlib.pyplot as plt
from sqlite3 import Error
sqlite_connection= None; #подклюение к бд
cursor=None; #курсор для работы с бд
bd="swot.db" #файл с бд
current_user=""; #текущий логин пользователя
current_project="";
types=["strengths","weaknesses","opportunities","threats"]
#создаем БД со всеми таблицами, вызывается единожды

def create_swot_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Swot(line integer, project integer,type text,"
                   "name text, action text, importance integer, probability integer,FOREIGN KEY (project) REFERENCES "
                   "Projects (id))")
    return True

def create_project_table():
    sqlite_select_query = """CREATE TABLE IF NOT EXISTS Projects (
        id integer PRIMARY KEY AUTOINCREMENT,
        login text NOT NULL,
        name text NOT NULL,
        FOREIGN KEY (login) REFERENCES Users(login)
    );"""
    cursor.execute(sqlite_select_query)
    return True

def create_user_table():
    sqlite_select_query = """CREATE TABLE IF NOT EXISTS Users (
        login text PRIMARY KEY,
        password text NOT NULL
    );"""
    cursor.execute(sqlite_select_query)
    return True

#Функция для получения информации по своту для каждой из категорий

def get_swot_data(type):
    sqlite_read_query = """select * from Swot where project =? and type=? """
    cursor.execute(sqlite_read_query, (current_project,type))
    tmp_res=cursor.fetchall()
    results=[]
    for res in tmp_res:
        row={}
        row["id"]=res[0]
        row["name"]=res[3]
        row["action"]=res[4]
        row["importance"]=res[5]
        row["probability"]=res[6]
        row["power"]=res[5]*res[6]
        results.append(row)
    return results
    # return [{id:n0,name:n1,action:n2,importance:n3,probability:n4,power:n5},{}]
#возвращает словарь с резулатом по каждому показателю {strengths:10,opportunities:9.. },а также общий результат по все показателям
def count_swot():
    swot={}
    for t in types:
        res=get_swot_data(t)
        tmp=[]
        for r in res:
            tmp.append(r["power"])
        swot[t]=sum(tmp)
    result=0
    for s in swot:
        if(s=="strengths" or s=="opportunities"):
            result=result+swot[s]
        else:
            result=result-swot[s]
    return swot,result








#Функция обновления информации по своту
def set_swot_data(line, type, name, action, importance, probability):
    sqlite_read_query = """select * from Swot where line =? and project=? and type=?"""
    cursor.execute(sqlite_read_query, (line, current_project, type))
    results = cursor.fetchall()
    if (len(results) != 0):
        sqlite_update_query = ("UPDATE Swot SET name = ?,action=?,importance=?,probability=? "
                               "WHERE  line =? and project=? and type=?")
        cursor.execute(sqlite_update_query, (name,action,importance,probability,line,current_project,type ))
    else:
        sqlite_insert_query = """insert into Swot values (?,?,?,?,?,?,?)"""
        cursor.execute(sqlite_insert_query, (line, current_project,type,name,action,importance,probability))
    #read Swot
    pass

def change_project(new_project): #выбираем из доступных проектов
    global current_project
    current_project = new_project
    return True

def create_new_project(new_project):  #new_project - название проекта
    sqlite_update_query = """insert into Projects (login,name) values (?,?)"""
    cursor.execute(sqlite_update_query, (current_user,new_project))
    global current_project
    current_project = new_project
    return True


def view_all_projects():
    sqlite_query = """select * from Projects where login=?"""
    cursor.execute(sqlite_query, (current_user,))
    return cursor.fetchall()

# read Users
def get_user_data(login):
    sqlite_read_query = """select * from Users where login =? """
    cursor.execute(sqlite_read_query, (login,))
    return cursor.fetchall()

#change Пользователи
def set_user_data(password):
    sqlite_update_query = """insert into Users values (?,?)"""
    cursor.execute(sqlite_update_query, (current_user, password))
    return True

#to log in
def sign_in(login, password):
    results = get_user_data(login) #get such user like [('darkur', 'ILOVEHSE')]
    if len(results) == 0: #if no such user
        raise KeyError("No such user")
    else:
        true_password = results[0][1]
        if true_password != password: #if password correct
            raise KeyError("Wrong password")
        else:
            global current_user
            current_user = login
            global current_project
            current_project = None
            return True

#зарегаться
def sign_up(login, password):
    results = get_user_data(login) #get such user like [('darkur', 'ILOVEHSE')]
    if len(results) == 1: #if user exists
        print(login)
        raise KeyError("User with such login exists")
    else:
        global current_user
        current_user = login
        set_user_data(password) #add new user
        return True



#функция для построения графиков
def get_sep_plot(type):
    swot = get_swot_data(type)
    index = []
    for n in swot:
        index.append(n['importance'])
    values = list(range(1, len(index)+1))
    plt.bar(values,index)
    plt.xticks(list(range(1, len(index)+1)))
    plt.grid(True)
    plt.show()

def get_com_plot():
    swot = count_swot()[0]
    index = []
    for value in swot.values():
        index.append(value)
    values = list(range(1, len(index) + 1))
    plt.bar(values, index)
    plt.xticks(list(range(1, len(index) + 1)))
    plt.grid(True)
    plt.show()








try:
    sqlite_connection = sqlite3.connect(bd)
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)


except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
''''
finally:
    if (sqlite_connection):
        cursor.close()
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
'''

create_user_table()
create_project_table()
create_swot_table()

get_com_plot()


sqlite_connection.commit()
cursor.close()
sqlite_connection.close()
print("Соединение с SQLite закрыто")


