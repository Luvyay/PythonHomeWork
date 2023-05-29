'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Данная программа иммеет следующий функционал:
1. Добавление контактов в файл phone.txt
2. Поиск контакта по файлу phone.txt (хотя бы по одному или по нескольким характеристикам: имя, фамилия, отчество или номер)
3. Отображение всех контактов
4. Отображение n количество контактов с конца файла
5. Отображение n количество контактов с начала файла
6. Изменение данных контакта (находит контакт хотя бы по одной или по нескольким характеристикам и дает возможность изменить сразу все)
7. Удаление контакта (находит нужный контакт и удаляет)
8. Выход из программы
'''

# Блок с константами

WRITE_CONTACT = 1
FIND_CONTACTS = 2
SHOW_CONTACTS = 3
SHOW_LAST = 4
SHOW_FIRST = 5
EDIT_CONTACT = 6
DELETE_CONTACT = 7
EXIT_PROG = 8
NAME_FILE = 'phone.txt'
KEY_TUPLE = ('name', 'surname', 'patronymic', 'number', 'id')

# Блок с вспомогательными функциями

def get_information():
    # Вспомогательная функция, которая получает информацию
    # от пользователя и записывает это в словарь

    dict_information = dict()
    dict_information['name'] = input('Введите имя: ')
    dict_information['surname'] = input('Введите фамилию: ')
    dict_information['patronymic'] = input('Введите отчество: ')
    dict_information['number'] = input('Введите номер телефона: ')

    print() # для читабельности в консоли

    return dict_information

def read_phone():
    # Вспомогательная функция, которая считывает данные из файла phone.txt, 
    # записывая информацию в список, где каждая новая строка 
    # это 1 элемент, который в свою очередь делится на словарь
    # И возвращает данный список, состоящий из словарей

    date = []
    with open(NAME_FILE, 'r', encoding='utf-8') as file:
        index = 1
        for line in file:
            line = line.rstrip() + ';' + str(index)
            line_dict = dict(zip(KEY_TUPLE, line.split(';')))
            date.append(line_dict)
            index += 1
    return date

def print_contacts(date):
    # Вспомогательная функция, которая принимает список состоящий из 
    # словарей и печатает в читаемом формате данные словари

    for item in date:
        print(f"{item['name']} {item['surname']} "
              f"{item['patronymic']} {item['number']}")

def alteration_for_edit(date, new_dict_information, index):
    # Вспомогательная функция, которая перезаписывает информацию
    # в phone.txt с измененными данными

    with open(NAME_FILE, 'w', encoding='utf-8') as file:
        for index_date in range(len(date)):
            if date[index_date]['id'] != index:
                file.write(f"{date[index_date]['name']};{date[index_date]['surname']};"
                        f"{date[index_date]['patronymic']};{date[index_date]['number']}\n")
            else:
                file.write(f"{new_dict_information['name']};{new_dict_information['surname']};"
                        f"{new_dict_information['patronymic']};{new_dict_information['number']}\n")

def alteration_for_delete(date, index):
    # Вспомогательная функция, которая перезаписывает файл
    # phone.txt без указанного контакта

    with open(NAME_FILE, 'w', encoding='utf-8') as file:
        for element in date:
            if element['id'] != index:
                file.write(f"{element['name']};{element['surname']};"
                        f"{element['patronymic']};{element['number']}\n")

def find_contacts(dict_information):
    # Вспомогательная функция, которая ищет контакт по имени, фамилии, отчеству или номеру

    date = read_phone()

    if dict_information['name'] == '' and dict_information['surname'] == '' and \
    dict_information['patronymic'] == '' and dict_information['number'] == '':
        res_date = ['no criteria']
    else:
        res_date = date.copy()
        for key in dict_information:
            if dict_information[key] != '':
                res_date = list(filter(lambda x: x[key] == dict_information[key], res_date))

    return res_date

# Блок с основными функциями

def delete_contact(date):
    # Функция, которая находит контакт для удаления и удаляет его

    dict_information = get_information()

    dict_of_found_contacts = find_contacts(dict_information)
    if len(dict_of_found_contacts) == 0:
        print('Совпадений не нашлось!')

    elif dict_of_found_contacts[0] == 'no criteria':
        print('Вы не ввели критерии для поиска!')

    elif len(dict_of_found_contacts) == 1:
        alteration_for_delete(date, dict_of_found_contacts[0]['id'])

        print(f"Контакт: {dict_of_found_contacts[0]['name']} {dict_of_found_contacts[0]['surname']} "
              f"{dict_of_found_contacts[0]['patronymic']} {dict_of_found_contacts[0]['number']} "
              "- был удален."
              )

    elif len(dict_of_found_contacts) > 1:
        print('Было найдено несколько совпадений!\n'
              'Выберите тот, который надо удалить и укажите его номер\n'
              '(начиная с верху; порядок начинается с 1):\n'
              )
        print_contacts(dict_of_found_contacts)
        index = int(input('Введите номер: '))

        alteration_for_delete(date, dict_of_found_contacts[index-1]['id'])

        print(f"Контакт: {dict_of_found_contacts[index-1]['name']} {dict_of_found_contacts[index-1]['surname']} "
              f"{dict_of_found_contacts[index-1]['patronymic']} {dict_of_found_contacts[index-1]['number']} "
              "- был удален."
              )

def edit_contact(date):
    # Функция, которая находит контакт для изменения
    # запрашивает новые данные и вносит изменения

    dict_information = get_information()

    dict_of_found_contacts = find_contacts(dict_information)
    if len(dict_of_found_contacts) == 0:
        print('Совпадений не нашлось!')

    elif dict_of_found_contacts[0] == 'no criteria':
        print('Вы не ввели критерии для поиска!')

    elif len(dict_of_found_contacts) == 1:
        print('Введите новые данные.')
        new_dict_information = get_information()
        alteration_for_edit(date, new_dict_information, dict_of_found_contacts[0]['id'])

        print("Контакт был изменен с:\n"
              f"{dict_of_found_contacts[0]['name']} {dict_of_found_contacts[0]['surname']} "
              f"{dict_of_found_contacts[0]['patronymic']} {dict_of_found_contacts[0]['number']}\n"
              "на:\n"
              f"{new_dict_information['name']} {new_dict_information['surname']} "
              f"{new_dict_information['patronymic']} {new_dict_information['number']}\n"
              )

    elif len(dict_of_found_contacts) > 1:
        print('Было найдено несколько совпадений!\n'
              'Выберите тот, который надо изменить и укажите его номер\n'
              '(начиная с верху; порядок начинается с 1):\n'
              )
        print_contacts(dict_of_found_contacts)
        index = int(input('Введите номер: '))

        print('Введите новые данные.')
        new_dict_information = get_information()
        alteration_for_edit(date, new_dict_information, dict_of_found_contacts[index-1]['id'])

        print("Контакт был изменен с:\n"
              f"{dict_of_found_contacts[index-1]['name']} {dict_of_found_contacts[index-1]['surname']} "
              f"{dict_of_found_contacts[index-1]['patronymic']} {dict_of_found_contacts[index-1]['number']}\n"
              "на:\n"
              f"{new_dict_information['name']} {new_dict_information['surname']} "
              f"{new_dict_information['patronymic']} {new_dict_information['number']}\n"
              )

def show_first(date):
    # Функция, которая отображает первые n записей, где
    # n указывает пользователь
    num_of_rec = int(input('Введите количество записей: '))
    print() # для читабельности в консоли

    if num_of_rec > len(date):
        num_of_rec = len(date)
    
    print_contacts(date[0:num_of_rec])

def show_last(date):
    # Функция, которая отображает последние n записей, где
    # n указывает пользователь
    num_of_rec = int(input('Введите количество записей: '))
    print() # для читабельности в консоли

    if num_of_rec > len(date):
        num_of_rec = len(date)
    
    print_contacts(date[-num_of_rec:len(date)])

def write_contact(dict_information):
    # Функция, которая записывает новый контакт в файл phone.txt

    with open(NAME_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{dict_information['name']};{dict_information['surname']};"
                   f"{dict_information['patronymic']};{dict_information['number']}\n")
    
    print(f"Контакт: {dict_information['name']} {dict_information['surname']} "
          f"{dict_information['patronymic']} {dict_information['number']}"
          " - был добавлен.")

def show_menu():
    # Функция, которая печатает на экран перечень возможностей
    # программы и возвращает номер меню

    print(
        '----------------------------------------------------\n'
        '1. Добавить новый контакт;\n'
        '2. Найти контакт;\n'
        '3. Показать весь справочник;\n'
        '4. Показать последние n записей;\n'
        '5. Показать первые n записей;\n'
        '6. Изменить контакт;\n'
        '7. Удалить контакт;\n'
        '8. Выход.\n'
        '----------------------------------------------------'
    )

    try:
        return int(input('Введите номер пункта меню: '))
    except Exception:
        return 99

def main():
    # Основная функция, которая анализирует что хочет сделать пользователь
    
    choice = show_menu()
    while choice != EXIT_PROG:
        if choice == WRITE_CONTACT:
            write_contact(get_information())

        elif choice == FIND_CONTACTS:
            dict_of_found_contacts = find_contacts(get_information())

            if len(dict_of_found_contacts) == 0:
                print('Совпадений не нашлось!')
            elif dict_of_found_contacts[0] == 'no criteria':
                print('Вы не ввели критерии для поиска!')
            else:
                print_contacts(dict_of_found_contacts)

        elif choice == SHOW_CONTACTS:
            print() # для читабельности в консоли
            print_contacts(read_phone())

        elif choice == SHOW_LAST:
            show_last(read_phone())

        elif choice == SHOW_FIRST:
            show_first(read_phone())

        elif choice == EDIT_CONTACT:
            edit_contact(read_phone())

        elif choice == DELETE_CONTACT:
            delete_contact(read_phone())

        else:
            print('Введено не корректное значение!')

        choice = show_menu()

if __name__ == '__main__':
    main()