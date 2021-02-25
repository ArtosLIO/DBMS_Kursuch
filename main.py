import mysql.connector
from mysql.connector import Error
from MySQLQuery import menu, select, insert, update, delete
from ShowQuery import prsel

connector = mysql.connector.connect()
item = False
i = 3
cikl = 0

while True:
    connuser = input('Введите имя пользователя: ')
    connpass = input('Введите пароль пользователя: ')

    try:
        connector = mysql.connector.connect(
            user=connuser,
            password=connpass,
            host='localhost',
            database='VoinskaChast'
        )
    except Error as e:
        print('Error connected: ', e)

    if connector.is_connected():
        print('Удачное подключение к MySQL \"Военная база\"')
        item = True
        break
    else:
        i -= 1
        if i == 0:
            print("Попытки входа исчерпаны.")
            break
        print("Неверный ввод логина или пароля.\nОсталось попыток " + str(i))

if item:

    print(menu(0))
    while item:
        foo = input('Введите символ для перехода к функции: ')

        if foo == 'e':

            item = False

        elif foo == 'i':

            print(menu(2))
            query = input('Введите символ: ')

            try:
                cursor = connector.cursor()
                cursor.execute(insert(query))
                if cursor.lastrowid:
                    print("Добаленный id", cursor.lastrowid)
                else:
                    print("Добаленный id не был найден")
                connector.commit()
            except Error as e:
                print(e)
            finally:
                cursor.close()
                print(menu(0))

        elif foo == 'u':

            print(menu(3))
            query = input('Введите символ: ')

            try:
                cursor = connector.cursor()
                cursor.execute(update(query))
                connector.commit()
            except Error as e:
                print(e)
            finally:
                cursor.close()
                print(menu(0))

        elif foo == 'd':

            print(menu(4))
            query = input('Введите символ: ')

            try:
                cursor = connector.cursor()
                cursor.execute(delete(query))
                connector.commit()
            except Error as e:
                print(e)
            finally:
                cursor.close()
                print(menu(0))

        elif foo == 's':

            print(menu(1))
            query = input('Введите символ: ')

            try:
                cursor = connector.cursor()
                cursor.execute(select(query))
                result = cursor.fetchone()
                while result is not None:
                    prsel(query, cikl, result)
                    result = cursor.fetchone()
                    if cikl == 0:
                        cikl += 1
            except Error as e:
                print(e)
            finally:
                cursor.close()
                wres = open("selrot.txt", "w")
                wres.close()
                cikl = 0
                print(menu(0))

        elif foo == 'm':

            print(menu(0))

        else:
            
            print("""Символ введен неверно, попробуйте еще раз.
Для повторного вывода меню введите (M)enu.
""")

if connector.is_connected():
    connector.close()
    print('Отключение от БД \"Военная база\"')

