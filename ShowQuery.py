
def prsel(item, cikl, result):

    if item == 'o':

        #print("ФИО: {} {} {}\tЗвание: {}\tДолжность: {}\tОклад: {}".format(result[0], result[1], result[2], result[3], result[4], result[5]))

        fio = result[0] + ' ' + result[1] + ' ' + result[2]
        if cikl != 0:
            print("{: ^45} | {: <20} | {: <25} | {}".format(fio, result[3], result[4], result[5]))
        else:
            print(" {: ^44} | {: ^20} | {: ^25} | {}".format('ФИО', 'Звание', 'Должность', 'Оклад'))
            print("-----------------------------------------------------------------------------------------------------------")
            print("{: ^45} | {: <20} | {: <25} | {}".format(fio, result[3], result[4], result[5]))

    elif item == 's':

        recruit = ''
        if result[3] == 0:
            recruit = 'Контрактник'
        else:
            recruit = 'Призывник'
        # print("ФИО: {} {} {}\t{}\tВзвод: {}".format(result[0], result[1], result[2], recruit, result[4]))
        fio = result[0] + ' ' + result[1] + ' ' + result[2]
        if cikl != 0:
            print("{: ^45} | {: <15} | {: <20}".format(fio, recruit, result[4]))
        else:
            print("{: ^45} | {: <15} | {: <20}".format('ФИО', '', 'Взвод'))
            print('-' * 90)
            print("{: ^45} | {: <15} | {: <20}".format(fio, recruit, result[4]))

    elif item == 'p':
        pass
    # rres = open("selrot.txt", "r")
    #
    # if result[0] != rres.read():
    #     print("Название Роты: \'{}\'\nКомандир Роты: {}\t{}\t{}".format(result[0], result[1], result[2], result[3]))
    #     print("\tНазвание Взвода: \'{}\'\t Количество солдат: {}\t Командир Взвода: {}\t{}\t{}".format(result[4], result[5], result[6], result[7], result[8]))
    #
    #     wres = open("selrot.txt", "w")
    #     wres.write(result[0])
    #     wres.close()
    # else:
    #     print("\tНазвание Взвода: \'{}\'\t Количество солдат: {}\t Командир Взвода: {}\t{}\t{}".format(result[4], result[5], result[6], result[7], result[8]))
    # rres.close()

    elif item == 'c':

        if result[4] == 2:
            print("\'{}\'\nСтарший Прапорщик: {}\t{}\t{}".format(result[0], result[1], result[2], result[3]))
        else:
            print("\t\tПрапорщик: {}\t{}\t{}".format(result[1], result[2], result[3]))

    elif item == 'r':

        print("\t{}\t Колическтво: {} {}\t Дата завоза: {}\tДата следущего завоза: {}".format(result[0], result[1], result[2], result[3], result[4]))

    elif item == 't':

        rres = open("selrot.txt", "r")

        if result[0] != rres.read():
            print("Название Отдела: {}\tКомандир Отдела: {}\t{}\t{}".format(result[0], result[1], result[2], result[3]))
            print("\tНазвание: {}\tОружие: {}\tБроня: {}\tТопливо: {}\tКоличество: {}\t\
            Проверка: {}\t".format(result[4], result[5], result[6], result[7], result[8], result[9]))

            wres = open("selrot.txt", "w")
            wres.write(result[0])
            wres.close()
        else:
            print("\tНазвание: {}\tОружие: {}\tБроня: {}\tТопливо: {}\tКоличество: {}\t\
            Проверка: {}\t".format(result[4], result[5], result[6], result[7], result[8], result[9]))

    elif item == 'x':

        rres = open("selrot.txt", "r")

        if result[0] != rres.read():
            print("Название Отдела: {}\tКомандир Отдела: {}\t{}\t{}".format(result[0], result[1], result[2], result[3]))
            print("\tНазвание: {}\tКоличество: {}\tПроверка: {}\t".format(result[4], result[5], result[6]))

            wres = open("selrot.txt", "w")
            wres.write(result[0])
            wres.close()
        else:
            print("\tНазвание: {}\tКоличество: {}\tПроверка: {}\t".format(result[4], result[5], result[6]))

    elif item == 'f':

        rres = open("selrot.txt", "r")

        if result[0] != rres.read():
            print("Название Отдела: {}\tКомандир Отдела: {}\t{}\t{}".format(result[0], result[1], result[2], result[3]))
            print("\tНазвание: {}\tКалибр: {}\tКоличество: {}\tПроверка: {}\t".format(result[4], result[5], result[6], result[7]))

            wres = open("selrot.txt", "w")
            wres.write(result[0])
            wres.close()
        else:
            print("\tНазвание: {}\tКалибр: {}\tКоличество: {}\tПроверка: {}\t".format(result[4], result[5], result[6], result[7]))

    elif item == 'z':
        if result[0] == None:
            print("Всего оффицеров: {}".format(result[1]))
        else:
            print("{}\tКоличество: {}".format(result[0], result[1]))

    elif item == 'k':
        print('''Всего солдат: {}
    призывкиков: {}
    контрактников: {}
'''.format(result[2], result[0], result[1]))

    elif item == 'd':
        print('''Вес продуктов: {:.3f} тонн
    Количество упаковок: {} штук'''.format(float(result[0]), result[1]))

    elif item == 'g':
        if result[0] == None:
            print("Всего техники: {}".format(result[2]))
        elif result[1] == None and result[0] != None:
            print("{}\tвсего: {}".format(result[0], result[2]))
        else:
            print("\t{}\tвсего {}".format(result[1], result[2]))

    elif item == 'y':
        if result[0] == None:
            print('''Всего оружия на складе: {}
    Ближнего оружия: {}
    Дальнего оружия: {}'''.format(int(result[1])+int(result[2]), int(result[1]), int(result[2])))
        elif result[2] == None:
            print('''{}\tвсего: {}'''.format(result[0], int(result[1])))
        else:
            print('''{}\tвсего: {}'''.format(result[0], int(result[2])))

    else:
        print("Error: Данной команды не существует!")

