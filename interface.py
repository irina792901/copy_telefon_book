def main():
    print('\n---------------------------------------------')
    main = '''Введите
    для чтения из телефонного справочника: 1
    для записи в телефонный справочник:    2
    для сохранения в файл:                 3
    для выхода:                            q'''
    print(main)
    return input("Ввод: ")

def disp():
    print('\n---------------------------------------------')
    disp = """Введите
    для вывода всего справочника:   1
    для поиск человека              2
    для выхода:                     q
    для возврата в предыдущее меню: r"""
    print(disp)
    return input("Ввод: ")

def imp():
    print('\n---------------------------------------------')
    imp = """Введите
    для добавить человека в справочник: 1
    для выхода:                     q
    для возврата в предыдущее меню: r"""
    print(imp)
    return input("Ввод: ")

def exp():
    print('\n---------------------------------------------')
    exp = """Введите
    для CVS:                        1
    для JSON:                       2
    для XML:                        3
    для выхода:                     q
    для возврата в предыдущее меню: r"""
    print(exp)
    return input("Ввод: ")

    