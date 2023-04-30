def TaskHomeWork1():
    # Заполните массив элементами арифметической прогрессии. Её первый элемент,
    # разность и количество элементов нужно ввести с клавиатуры.
    # Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
    # Каждое число вводится с новой строки.

    start_list = int(input('Please enter the start of list: '))
    step_of_list = int(input('Please enter the step of list: '))
    amount_of_list = int(input('Please enter the amount of list: '))
    end_of_list = start_list + step_of_list * amount_of_list

    some_list = [i for i in range(start_list, end_of_list, step_of_list)]

    print(some_list)

def TaskHomeWork1Alternative():
    # Заполните массив элементами арифметической прогрессии. Её первый элемент,
    # разность и количество элементов нужно ввести с клавиатуры.
    # Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
    # Каждое число вводится с новой строки.

    start_list = int(input('Please enter the start of list: '))
    step_of_list = int(input('Please enter the step of list: '))
    amount_of_list = int(input('Please enter the amount of list: '))
    end_of_list = start_list + step_of_list * amount_of_list

    print(*range(start_list, end_of_list, step_of_list))

def TaskHomeWork2():
    # Определить индексы элементов массива (списка), значения
    # которых принадлежат заданному диапазону (т.е. не меньше
    # заданного минимума и не больше заданного максимума)

    amount_of_list = int(input('Please enter the amount of list: '))
    some_list = [int(input('Please enter the value: ')) for _ in range(amount_of_list)]

    print(some_list)

    lower_limit = int(input('Please enter the lowe limit: '))
    upper_limit = int(input('Please enter the upper limit: '))

    result_list = []

    for i in range(len(some_list)):
        if lower_limit <= some_list[i] <= upper_limit:
            result_list.append(i)
    
    print(result_list)

