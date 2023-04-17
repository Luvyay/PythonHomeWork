import random

def Task1():
    # На столе лежат n монеток. Некоторые из них лежат вверх
    # решкой, а некоторые – гербом. Определите минимальное число
    # монеток, которые нужно перевернуть, чтобы все монетки были
    # повернуты вверх одной и той же стороной. Выведите минимальное
    # количество монет, которые нужно перевернуть

    amount_of_money = int(input('Please enter amount: '))

    eagle = 0
    tails = 0

    for _ in range(amount_of_money):
        coin = random.randint(0, 1)
        print(coin, end=' ')

        if coin == 0:
            tails += 1
        else:
            eagle += 1
        
    print()

    if tails == eagle:
        print(f'The number of tails and eagle is the same ({tails}).')
    elif tails < eagle:
        print(tails)
    else:
        print(eagle)

def Task2():
    # Петя и Катя – брат и сестра. Петя – студент, а Катя –
    # школьница. Петя помогает Кате по математике. Он задумывает два
    # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
    # этого Петя делает две подсказки. Он называет сумму этих чисел S и их
    # произведение P. Помогите Кате отгадать задуманные Петей числа.

    sum = int(input('Please enter the sum: '))
    multi = int(input('Please enter the multi: '))
    flag_completed = False

    for x in range(1, 10):
        if not flag_completed:
            for y in range(1, 10):
                if x + y == sum and x * y == multi:
                    print(f'desired numbers {x}; {y}')
                    flag_completed = True
                    break

def Task3():
    # Требуется вывести все целые степени двойки (т.е. числа
    # вида 2k), не превосходящие числа N.

    number = int(input('Please enter the number: '))

    result = 1

    while result < number:
        print(result, end=' ')
        result *= 2
    
    print()


