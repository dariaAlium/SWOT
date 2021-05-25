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
    print("def create_new_project(new_project)")
    sqlite_update_query = """insert into Projects (login,name) values (?,?)"""
    cursor.execute(sqlite_update_query, (current_user,new_project))
    print(cursor.fetchall())
    global current_project
    current_project = new_project
    return True


def view_all_projects():
    sqlite_query = """select name from Projects where login=?"""
    print("Projects")
    #sqlite_query = """select * from Projects"""
    cursor.execute(sqlite_query,(current_user))
    results = [i[0] for i in cursor.fetchall()]
    print("results: ")
    print(results)
    return results

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
    print("sign_in")
    results = get_user_data(login) #get such user like [('darkur', 'ILOVEHSE')]
    print(results)
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
    fig = plt.bar(values,index)
    plt.xticks(list(range(1, len(index)+1)))
    plt.grid(True)
    plt.show()
    return 'sep_plot.png'

def get_com_plot():
    swot = count_swot()[0]
    index = []
    for value in swot.values():
        index.append(value)
    values = list(range(1, len(index) + 1))
    fig = plt.bar(values, index)
    plt.xticks(list(range(1, len(index) + 1)))
    plt.grid(True)
    plt.show()
    #fig.savefig('com_plot.png')
    return 'com_plot.png'

def create_proceeds_table():
    sqlite_select_query = """CREATE TABLE IF NOT EXISTS proceedsPlan (
        line integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        project integer NOT NULL,
        service text NOT NULL,
        price integer NOT NULL,
        amount_per_year integer NOT NULL,
        FOREIGN KEY (project) REFERENCES Projects (id)
    );"""
    cursor.execute(sqlite_select_query)
    return True


def create_salary_table():
    sqlite_select_query = """CREATE TABLE IF NOT EXISTS salary (
        line integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        project integer NOT NULL,
        occupation text NOT NULL,
        payment integer NOT NULL,
        revenue_percentage integer,
        tax integer NOT NULL,
        insurance integer NOT NULL,
        FOREIGN KEY (project) REFERENCES Projects (id)
    );"""
    cursor.execute(sqlite_select_query)
    return True


def create_loan_table():
    sqlite_select_query = """CREATE TABLE IF NOT EXISTS loan (
        line integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        project integer NOT NULL,
        credit_sum integer NOT NULL,
        percentage integer NOT NULL,
        period NOT NULL,
        FOREIGN KEY (project) REFERENCES Projects (id)
    );"""
    cursor.execute(sqlite_select_query)
    return True


def create_expenses_table():
    sqlite_select_query = """CREATE TABLE IF NOT EXISTS expensesPlan (
        line integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        project integer NOT NULL,
        name text NOT NULL,
        cost integer NOT NULL,
        FOREIGN KEY (project) REFERENCES Projects (id)
    );"""
    cursor.execute(sqlite_select_query)
    return True

#посчитать плановый доход
def get_proceeds_data():
    global current_project
    current_project = 1
    sqlite_read_query = """select * from proceedsPlan where project = ?"""
    #id project service price amount
    cursor.execute(sqlite_read_query, current_project)
    tmp_res = cursor.fetchall()
    if len(tmp_res) != 0:
        result = {"total": 0}
        for res in tmp_res:
            result["total"] = result["total"] + res[3]*res[4]
        return result
    # return {total: n0}


#Функция добавления информации по доходам
def set_proceeds_data(service, price, amount):
    global current_project
    current_project=1
    sqlite_insert_query = """insert into proceedsPlan (project, service, price, amount_per_year) values (?,?,?,?)"""
    cursor.execute(sqlite_insert_query, (current_project, service, price, amount))


#посчитать зарплатные затраты
def get_salary_data():
    sqlite_read_query = """select * from salary where project = ?"""
    #id project occupation perm_salary revenue_percentage tax insurance
    cursor.execute(sqlite_read_query, current_project)
    tmp_res = cursor.fetchall()
    if len(tmp_res) != 0:
    #если бд не пустая
        proceed = get_proceeds_data()
        if len(proceed) != 0:
            result = []
            for res in tmp_res:
                row = {"perm_salary": res[3],
                       "temp_salary": res[4] * proceed["total"] / 100}
                row["all_salary"] = row["perm_salary"] + row["temp_salary"]
                row["tax_value"] = row["all_salary"]*res[5]/100
                row["insurance_value"] = row["all_salary"]*res[6]/100
                row["all_payment"] = row["all_salary"] + row["insurance_value"]
                result.append(row)
            return result
    # return [{perm_salary: n0, temp_salary: n1, all_salary: n2, ..}, {..}]


#Функция добавления информации по зарплате
def set_salary_data(occupation, perm_salary, revenue_percentage, tax, insurance):
    sqlite_insert_query = """insert into salary (project, occupation, payment, 
    revenue_percentage, tax, insurance) values (?,?,?,?,?,?)"""
    cursor.execute(sqlite_insert_query, (current_project, occupation, perm_salary, revenue_percentage, tax, insurance))


#посчитать кредит
def get_loan_data():
    sqlite_read_query = """select * from loan where project = ?"""
    #id project credit_sum percentage period
    cursor.execute(sqlite_read_query, current_project)
    tmp_res = cursor.fetchall()
    if len(tmp_res) != 0:
        result = {"total": 0, "overpay": 0} #если кредитов несколько, все посчитаются в одну кучу
        for res in tmp_res:
            result["overpay"] = result["overpay"] + res[2]*res[3]*res[4]
            result["total"] = result["total"] + res[2] + result["overpay"]
        return result
    # return {overpay: n0, total: n1}


#Функция добавления информации по кредиту
def set_loan_data(credit_sum, percentage, period):
    sqlite_insert_query = """insert into loan (project, credit_sum, percentage, period) values (?,?,?,?)"""
    cursor.execute(sqlite_insert_query, (current_project, credit_sum, percentage, period))


#посчитать планируемые расходы
def get_expenses_data():
    sqlite_read_query = """select * from expensesPlan where project = ?"""
    #id project name cost
    cursor.execute(sqlite_read_query, current_project)
    tmp_res = cursor.fetchall()
    if len(tmp_res) != 0:
        result = {"total": 0}
        for res in tmp_res:
            result["total"] = result["total"] + res[2]*res[3]
        return result
    # return {total: n0}


#Функция добавления информации по планируемым расходам
def set_expenses_data(name, cost):
    sqlite_insert_query = """insert into expensesPlan (project, name, cost) values (?,?,?)"""
    cursor.execute(sqlite_insert_query, (current_project, name, cost))


def for_closing():
    sqlite_connection.commit()

def init_conn():
    sqlite_connection = sqlite3.connect(bd)
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)

    create_user_table()
    create_project_table()
    create_swot_table()
    create_proceeds_table()
    create_salary_table()
    create_loan_table()
    create_expenses_table()

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

#create_user_table()
#create_project_table()
#create_swot_table()


#sqlite_connection.commit()
#cursor.close()
#sqlite_connection.close()
#print("Соединение с SQLite закрыто")


