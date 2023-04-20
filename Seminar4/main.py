def Task1():
    # Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
    # Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
    # Пользователь вводит 2 числа. n — кол-во элементов первого множества.
    # m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

    amount_of_list_one = int(input('Please enter the amount of list 1: '))
    amount_of_list_two = int(input('Please enter the amount of list 2: '))

    print('Completing 1 list.')
    some_list_one = [int(input('Please enter the value: ')) for _ in range(amount_of_list_one)]
    print('Completing 2 list.')
    some_list_two = [int(input('Please enter the value: ')) for _ in range(amount_of_list_two)]

    print(some_list_one)
    print(some_list_two)

    some_set_one = set(some_list_one)
    some_set_two = set(some_list_two)

    result_list = list(some_set_one & some_set_two)

    result_list.sort()

    print(result_list)

def Task2():
    # В фермерском хозяйстве в Карелии выращивают чернику.
    # Она растёт на круглой грядке, причём кусты высажены только по окружности.
    # Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
    # Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
    # В этом фермерском хозяйстве внедрена система автоматического сбора черники.
    # Эта система состоит из управляющего модуля и нескольких собирающих модулей.
    # Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
    # Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
    # находясь перед некоторым кустом заданной во входном файле грядки.

    amount_of_bushes = int(input('Please enter the amount of bushes: '))
    harvest_of_bushes = [int(input(f'Please enter the harvest {i} bush: ')) for i in range(1, amount_of_bushes + 1)]

    print(harvest_of_bushes)

    if len(harvest_of_bushes) < 3:
        max_harvest = 0

        for item in harvest_of_bushes:
            max_harvest += item
    else:
        max_harvest = harvest_of_bushes[amount_of_bushes - 2] + harvest_of_bushes[amount_of_bushes - 1] + harvest_of_bushes[0]

        for index in range(len(harvest_of_bushes) - 1):
            if harvest_of_bushes[index - 1] + harvest_of_bushes[index] + harvest_of_bushes[index + 1] > 0:
                max_harvest = harvest_of_bushes[index - 1] + harvest_of_bushes[index] + harvest_of_bushes[index + 1]
    
    print(max_harvest)


