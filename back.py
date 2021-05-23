import sqlite3




#Функция для получения информации по своту для каждой из категорий
def get_swot_data():
    #read Swot
    pass
    # return [{id:n0,name:n1,action:n2,importance:n3,probability:n4,power:n5},{}]

#Функция обновления информации по своту
def set_swot_data():
    #read Swot
    pass


# read Users
def get_user_data(cursor, login):
    sqlite_read_query = """select * from Users where login =? """
    cursor.execute(sqlite_read_query, (login,))
    return cursor.fetchall()


#change Пользователи
def set_user_data(login, password):
    sqlite_update_query = """insert into Users values (?,?,?)"""
    pass

#to log in
def sign_in(cursor, login, password):
    results = get_user_data(cursor, login) #get such user like [(1, 'darkur', 'ILOVEHSE')]
    if len(results) == 0: #if no such user
        raise KeyError("No such user")
    else:
        true_password = results[0][0][2]
        if true_password != password: #if password correct
            raise KeyError("Wrong password")
        else:
            return True

#зарегаться
def sign_up(login, password):
    results = get_user_data(cursor, login) #get such user like [(1, 'darkur', 'ILOVEHSE')]
    if len(results) == 1: #if user exists
        raise KeyError("User with such login exists")
    else:
        pass
    #get_user_data(login)
    #check if the person exist
    #if not set_user_data(login)


#функция для построения графиков
def get_plot():
    pass


try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")