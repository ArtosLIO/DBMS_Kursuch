def menu(item):
    menu = ''

    if item == 0:
        menu = '''
    Как у пользователя у вас есть доступ к таким функциям:
    1) (I)nsert Введение данных в БД;
    2) (U)pdate Обновленние данных в БД;
    3) (D)elete Удаление данных в БД;
    4) (S)elect Показать данные с БД;
    5) (M)enu Повторный вывод меню;
    6) (E)xit Выход с приложения.
    '''

    elif item == 1:
        menu = '''
    Возможен вывод данных:
    1) (O) Информация об оффицерах;
    2) (S) Информация о солдатах;
    3) (P) Информация о Ротах;
    4) (C) Информация о Складах;
    5) (R) Информация о Продуктовом Складе;
    6) (T) Информация о Складе Техники;
    7) Информация о Складе Оружия;
        (X) Склад холодного оружия
        (F) Склад огнестрельного оружия
    8) Статистика.
        (Z) Вывести количество оффицеров каждого званияы
        (K) Вывести количество призывников и контрактников
        (D) Вывести количество продуктов
        (G) Вывести количество техники
        (Y) Вывести количество оружия
    '''

    elif item == 2:
        menu = '''
    Можете ввести данные в таблицы:
    1) (O) Оффицеры
    2) (C) Солдаты
    3) (R) Роты
    4) (B) Взводы
    5) (P) Продуктовый Склад
    6) (T) Склад Техники
    7) Склад Оружия:
        (X) Холодное оружие
        (F) Огнестрельное оружие 
    '''

    elif item == 3:
        menu = '''
    Можете обновить данные с таблицы:
    1) (O) Оффицеры
    2) (C) Солдаты
    3) (R) Роты
    4) (B) Взводы
    5) (P) Продуктовый Склад
    6) (T) Склад Техники
    7) Склад Оружия:
        (X) Холодное оружие
        (F) Огнестрельное оружие
    '''

    elif item == 4:
        menu = '''
    Можете удалить данные с таблицы:
    1) (O) Оффицеры
    2) (C) Солдаты
    3) (R) Роты
    4) (B) Взводы
    5) (P) Продуктовый Склад
    6) (T) Склад Техники
    7) Склад Оружия:
        (X) Холодное оружие
        (F) Огнестрельное оружие
    '''




    return menu


def select(item):
    select = ''

    if item == 'o':
        select = '''
            SELECT surname, name, patronymic, officerRank, position, salary
            FROM OfficerConsist as oc JOIN Position as p
            ON oc.id_position = p.id_position
            ORDER BY officerRank, surname DESC;
            '''

    elif item == 's':
        select = '''
            SELECT surname, name, patronymic, recruit, namePlatoon
            FROM SoldierConsist AS sc JOIN Platoon AS p
            ON sc.id_platoon = p.id_platoon
            ORDER BY recruit DESC, surname;
            '''

    elif item == 'p':
        select = '''
            SELECT nameCompany, oc.surname, oc.name, oc.patronymic, nameplatoon, kolvo, o.surname, o.name, o.patronymic
            FROM platoon AS p JOIN company AS c JOIN officerconsist AS oc
            ON c.id_officer = oc.id_officer AND p.id_company = c.id_company
            JOIN officerconsist as o on o.id_officer = p.id_officer
            ORDER BY 1;
            '''

    elif item == 'c':
        select = '''
            SELECT s.nameStock, oc.surname, oc.name, oc.patronymic, oc.id_position
            FROM officerconsist AS oc JOIN stock AS s ON s.id_officer = oc.id_officer
            UNION SELECT s.nameStock, oc.surname, oc.name, oc.patronymic, oc.id_position
            FROM stock AS s JOIN officerconsist AS oc JOIN transportstock AS tr 
            ON oc.id_officer = tr.id_officer AND s.id_stock = tr.id_stock
            UNION SELECT s.nameStock, oc.surname, oc.name, oc.patronymic, oc.id_position
            FROM stock AS s JOIN officerconsist AS oc JOIN zbroyastock AS zb 
            ON oc.id_officer = zb.id_officer AND s.id_stock = zb.id_stock
            GROUP BY 1,2,3,4,5
            ORDER BY nameStock, id_position DESC;
            '''

    elif item == 'r':
        select = '''
            SELECT name, mass, unit, datedelivery, timelife
            FROM productstock;
            '''

    elif item == 't':
        select = '''
            SELECT tr.name, o.surname, o.name, o.patronymic, id_type, zbroya, armor, fuel, kolvo, checkup
            FROM transportstock AS tr JOIN officerconsist AS o JOIN type AS t 
            ON tr.id_officer = o.id_officer AND tr.id_transport = t.id_transport;
            '''

    elif item == 'x':
        select = '''
            SELECT z.name, o.surname, o.name, o.patronymic, n.name, n.kolvo, n.checkup
            FROM zbroyastock AS z JOIN officerconsist AS o JOIN nearzbroya AS n
            ON z.id_officer = o.id_officer AND n.id_zbroya = z.id_zbroya;
            '''

    elif item == 'f':
        select = '''
            SELECT z.name, o.surname, o.name, o.patronymic, f.id_firearms, f.caliber, f.kolvo, f.checkup
            FROM zbroyastock AS z JOIN officerconsist AS o JOIN firearms AS f
            ON z.id_officer = o.id_officer AND f.id_zbroya = z.id_zbroya
            ORDER BY 1;
            '''

    elif item == 'z':
        select = '''SELECT officerrank, COUNT(officerrank) FROM officerconsist
GROUP BY 1 WITH ROLLUP ORDER BY 1;
        '''

    elif item == 'k':
        select = '''SELECT COUNT(recruit), 
(SELECT COUNT(recruit) FROM soldierconsist WHERE recruit = 0),
(SELECT COUNT(recruit) FROM soldierconsist)
FROM soldierconsist WHERE recruit = 1;
        '''

    elif item == 'd':
        select = '''SELECT sum(mass) + 
(SELECT SUM(mass) / 1000 FROM ProductStock WHERE unit = 'кг'),
(SELECT SUM(mass) FROM ProductStock WHERE unit = 'штук')
FROM ProductStock WHERE unit = 'т';
        '''

    elif item == 'g':
        select = '''SELECT name, id_type, sum(kolvo) from TransportStock as ts left join type as t
on ts.id_transport = t.id_transport
group by 1, 2 with rollup
order by 1, 2;
        '''

    elif item == 'y':
        select = '''SELECT z.name, sum(n.kolvo), sum(f.kolvo) FROM ZbroyaStock AS z LEFT JOIN nearZbroya AS n
ON z.id_zbroya = n.id_zbroya
left JOIN firearms AS f on z.id_zbroya = f.id_zbroya
group by 1 with rollup
order by 1;
        '''

    else:
        print("Error: Данной команды не существует!")

    return select


def insert(item):
    insert = ''

    if item == 'o':
        value = []
        value.append(input("Введите фамилию: "))
        value.append(input("\tИмя: "))
        value.append(input("\tОтчество: "))
        print("Возможны звания: Прапорщик, Старший Прапорщик, Лейтенант, Капитан, Майор, Подполковник, Полковник.")
        value.append(input("\tЗвание: "))
        print('''Возможны должности:
    (1) Заведующий Склада
    (2) Начальник Склада
    (3) Зам.Командира Взвода
    (4) Командир Учебного Взвода
    (5) Командир Взвода
    (6) Зам.Командира Роты
    (7) Командир Учебной Роты
    (8) Командир Роты
              ''')
        value.append(input("Должность: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO OfficerConsist (surname, name, patronymic, officerRank, id_position)
        VALUE (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'''.format(value[0], value[1], value[2], value[3], value[4])

    elif item == 'c':
        value = []
        value.append(input("Введите фамилию: "))
        value.append(input("\tИмя: "))
        value.append(input("\tОтчество: "))
        value.append(input("(0) Контрактник\n(1) Призывник\nВведите значение: "))
        value.append(input("Введите название взвода: "))

        if 'e' in value or '' in value:
            return

        insert = '''
call ins(\'{pl}\',\'{sur}\' ,\'{nam}\' ,\'{pat}\' ,\'{rec}\');
'''.format(sur=value[0], nam=value[1], pat=value[2], rec=value[3], pl=value[4])

    elif item == 'r':
        value = []
        value.append(input("Введите название Роты: "))
        value.append(input("Введите Фамилию оффицера: "))
        value.append(input("Введите имя оффицера: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO Company (nameCompany, id_officer)
VALUE (\'{}\' ,(select id_officer from officerconsist where surname = \'{}\' and name = \'{}\'))'''.format(value[0],
                                                                                                           value[1],
                                                                                                           value[2])

    elif item == 'b':
        value = []
        value.append(input("Введите название Взвода: "))
        value.append(input("Введите фимилию оффицера: "))
        value.append(input("Введите имя оффицера: "))
        value.append(input("Введите название Роты: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO platoon (nameplatoon, kolvo, id_officer, id_company) VALUE (\'{}\', 0, 
(SELECT id_officer FROM officerconsist WHERE surname = \'{}\' AND name = \'{}\'),
(SELECT id_company FROM company WHERE namecompany = \'{}\'));'''.format(value[0], value[1], value[2], value[3])

    elif item == 'p':
        value = []
        value.append(input("Введите название продукта: "))
        value.append(input("Введите количество: "))
        value.append(input("Введите единицу измерения: "))
        value.append(input("Введите дату следующей поставки: "))
        value.append(input("Введите название склада: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO productstock (name, mass, unit, DateDelivery, TimeLife, id_stock)
value (\'{}\', \'{}\', \'{}\', date(now()), \'{}\', 
(SELECT id_stock FROM Stock WHERE namestock = \'{}\'));'''.format(value[0], value[1], value[2], value[3], value[4])

    elif item == 't':
        value = []
        value.append(input("Введите название транспорта: "))
        value.append(input("Введите вооружение транспорта:"))
        value.append(input("Введите броню транспорта: "))
        value.append(input("Введите тип топлва: "))
        value.append(input("Введите тип транспорта: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO type (id_type, zbroya, armor, fuel, kolvo, checkup, id_transport)
VALUE (\'{}\', \'{}\', \'{}\', \'{}\', 0, date(now()), 
(SELECT id_trnsport FROM transportstock WHERE name = \'{}\'));'''.format(value[0], value[1], value[2], value[3],
                                                                         value[4])

    elif item == 'x':
        value = []
        value.append(input("Введите название оружие: "))
        value.append(input("Введите тип оружия: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO nearzbroya (name, kolvo, checkup, id_zbroya)
VALUE (\'{}\', \'0\', date(now()), 
(SELECT id_zbroya FROM zbroyastock WHERE name = \'{}\'))'''.format(value[0], value[1])

    elif item == 'f':
        value = []
        value.append(input("Введите название оружие: "))
        value.append(input("Введите калибр: "))
        value.append(input("Введите тип оружия: "))

        if 'e' in value or '' in value:
            return

        insert = '''INSERT INTO firearms (id_firearms, caliber, checkup, kolvo, id_zbroya)
VALUE (\'{}\', \'{}\', date(now()), \'0\',
(SELECT id_zbroya FROM zbroyastock WHERE name = \'{}\'))'''.format(value[0], value[1], value[2])

    else:
        print("Error: Данной команды не существует!")

    return insert


def delete(item):
    delete = ''

    if item == 'o':
        value = []
        value.append(input("Введите фимилию офицера: "))
        value.append(input("Введите имя офицера: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM OfficerConsist 
WHERE surname = \'{}\' AND name = \'{}\''''.format(value[0], value[1])

    elif item == 'c':
        value = []
        value.append(input("Введите фамилию солдата: "))
        value.append(input("Введите имя солдата: "))

        if 'e' in value or '' in value:
            return

        delete = '''
call del(\'{sur}\', \'{nam}\');
'''.format(sur=value[0], nam=value[1])

    elif item == 'r':
        value = []
        value.append(input("Введите название Роты: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM Company
WHERE nameCompany = \'{}\''''.format(value[0])

    elif item == 'b':
        value = []
        value.append(input("Введите название Взвода: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM Platoon
WHERE namePlatoon = \'{}\''''.format(value[0])

    elif item == 'p':
        value = []
        value.append(input("Введите название продукта: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM ProductStock
WHERE name = \'{}\''''.format(value[0])

    elif item == 't':
        value = []
        value.append(input("Введите название техники: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM Type
WHERE id_type = \'{}\''''.format(value[0])

    elif item == 'x':
        value = []
        value.append(input("Введите название оружия: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM nearZbroya
WHERE name = \'{}\''''.format(value[0])

    elif item == 'f':
        value = []
        value.append(input("Введите название оружия: "))

        if 'e' in value or '' in value:
            return

        delete = '''DELETE FROM firearms
WHERE id_firearms = \'{}\''''.format(value[0])

    else:
        print("Error: Данной команды не существует!")

    return delete


def update(item):
    update = ''

    if item == 'o':
        value = []
        value.append(input("Введите данные оффицера:\n\tФамилия оффицера: "))
        value.append(input("\tИмя оффицера: "))
        print("Возможны звания: Прапорщик, Старший Прапорщик, Лейтенант, Капитан, Майор, Подполковник, Полковник.")
        value.append(input("Введите новые данные:\n\tЗвание: "))
        print('''Возможны должности:
    (1) Заведующий Склада
    (2) Начальник Склада
    (3) Зам.Командира Взвода
    (4) Командир Учебного Взвода
    (5) Командир Взвода
    (6) Зам.Командира Роты
    (7) Командир Учебной Роты
    (8) Командир Роты''')
        value.append(input("\tДолжность: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE OfficerConsist
SET officerRank = \'{}\', id_position = \'{}\'
WHERE sername = \'{}\' AND name = \'{}\''''.format(value[2], value[3], value[0], value[1])

    elif item == 'c':
        value = []
        value.append(input("Введите данные солдата:\n\tФамилия солдата: "))
        value.append(input("\tИмя солдата: "))
        value.append(input("Введите новые данные:\n(0) Контрактник\n(1) Призывник\n\tВведите значение: "))
        value.append(input("\tВведите название взвода: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE SoldierConsist
SET recruit = \'{}\', 
id_platoon = (SELECT id_platoon FROM Platoon WHERE nameplatoon = \'{}\')
WHERE surname = \'{}\' AND name \'{}\''''.format(value[2], value[3], value[0], value[1])

    elif item == 'r':
        value = []
        value.append(input("Введите данные Роты:\n\tВведите название Роты: "))
        value.append(input("Введите новые данные:\n\tВведите название Роты: "))
        value.append(input("\tВведите Фамилию оффицера: "))
        value.append(input("\tВведите Имя оффицера: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE Company
SET nameCompany = \'{}\', 
id_officer = (SELECT id_officer FROM OfficerConsist WHERE surname = \'{}\' AND name = \'{}\')
WHERE nameCompany = \'{}\''''.format(value[1], value[2], value[3], value[0])

    elif item == 'b':
        value = []
        value.append(input("Введите данные Взвода:\n\tВведите название Взвода: "))
        value.append(input("Введите новые данные:\n\tВведите название Взвода: "))
        value.append(input("\tВведите название Роты: "))
        value.append(input("\tВведите фамилию оффицера: "))
        value.append(input("\tВведите имя оффицера: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE Platoon
SET namePlatoon = \'{}\', 
id_company = (SELECT id_company FROM company WHERE namecompany = \'{}\'),
id_officer = (SELECT id_officer FROM officerconsist WHERE surname = \'{}\' AND name = \'{}\')
WHERE namePlatoon = \'{}\''''.format(value[1], value[2], value[3], value[4], value[0])

    elif item == 'p':
        value = []
        value.append(input("Введите название продукта: "))
        value.append(input("\tВведите количество: "))
        value.append(input("\tВведите дату следующей поставки: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE ProductStock
SET mass = \'{}\', TimeLife = \'{}\', DateDelivery = date(now())
WHERE name = \'{}\''''.format(value[1], value[2], value[0])

    elif item == 't':
        value = []
        value.append(input("Введите название техники: "))
        value.append(input("\tВведите новое количество техники: "))
        value.append(input("\tВведите дату проверки: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE Type
SET kolvo = \'{}\', checkup = \'{}\'
WHERE id_type = \'{}\''''.format(value[1], value[2], value[0])

    elif item == 'x':
        value = []
        value.append(input("Введите название оружия: "))
        value.append(input("\tВведите количество оружия: "))
        value.append(input("\tВведите дату проверки: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE nearZbroya
SET kolvo = \'{}\', checkup = \'{}\'
WHERE name = \'{}\''''.format(value[1], value[2], value[0])

    elif item == 'f':
        value = []
        value.append(input("Введите название оружия: "))
        value.append(input("\tВведите количество оружия: "))
        value.append(input("\tВведите дату проверки: "))

        if 'e' in value or '' in value:
            return

        update = '''UPDATE firearms
SET kolvo = \'{}\', checkup = \'{}\'
WHERE id_firearms = \'{}\''''.format(value[1], value[2], value[0])

    else:
        print("Error: Данной команды не существует!")

    return update
