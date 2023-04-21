def Pow_number(number, degree):
    if degree == 1:
        return number
    return Pow_number(number, degree - 1) * number

def Task1():
    # Напишите программу, которая на вход принимает два числа A и B,
    # и возводит число А в целую степень B с помощью рекурсии.

    number = int(input('Please enter the number: '))
    degree = int(input('Please enter the degree: '))

    print(Pow_number(number, degree))

def RLE(string):
    # Блок со списком элементов, которые допускаются для сжатия

    setting_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']   
    
    # Блок на проверку корректности строки

    flag_wrong = False
    
    for item in set(string):
        if item not in setting_list:
            flag_wrong = True
    
    if not string:
        return 'The text is empty!'
    elif flag_wrong or string[0].isdigit():
        return 'The text is wrong!'
    
    # Формируем 2 списка (ключ и количество повторов)

    key_list = []
    count_list = []

    key_list.append(string[0])
    count_list.append(1)

    for index in range(1, len(string)):
        if string[index] == key_list[-1]:
            count_list[-1] += 1
        else:
            key_list.append(string[index])
            count_list.append(1)
    
    # Объединяем 2 списка с условием, что если элемент встречается 1 раз
    # то не указываем "1"

    result = ''

    for index in range(len(key_list)):
        if count_list[index] == 1:
            result += key_list[index]
        else:
            result += key_list[index] + str(count_list[index])
    
    return result
        
def UNRLE(string):    
    # Разбиваем нашу строчку на 2 списка (ключ и количество повторов)

    key_list = []
    count_list = []
    key_list.append(string[0])
    temp_count = ''
    

    for index in range(1, len(string)):
        if string[index].isdigit():
            temp_count += string[index]
        else:
            key_list.append(string[index])
            count_list.append(temp_count)
            temp_count = ''
    
    # Если последний ключ содержал количество повторений, но мы не записали количество повторений

    if temp_count:
        count_list.append(temp_count)
        temp_count = ''
    
    # Если последний элемент это ключ и был без повторений, то записываем пустую строчку

    if not string[-1].isdigit():
        count_list.append(temp_count)

    # Блок со списком элементов, которые допускаются для распаковки

    setting_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
    
    # Проверяем, что среди ключей находятся только доступные элементы

    flag_wrong = False

    for item in set(key_list):
        if item not in setting_list:
            flag_wrong = True
    
    if flag_wrong:
        return 'The text is wrong!'

    # Раскрываем сжатую строчку опираясь на 2 списка (ключ и количество повторов)

    result = ''
    
    for index in range(len(key_list)):
        if count_list[index]:
            result += key_list[index] * int(count_list[index])
        else:
            result += key_list[index]
    
    return result

def Task2():
    # Дана строка (возможно, пустая), состоящая из букв A-Z:
    # AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
    # Нужно написать функцию RLE которая на выходе даст строку вида: 
    # A4B3C2XYZD4E3F3A6B28
    # И сгенерирует ошибку, если на вход пришла невалидная строка.
    # Пояснения: Если символ встречается 1 раз, он остается без изменений;
    # Если символ повторяется более 1 раза, к нему добавляется количество
    # повторений.

    package_str = input('Please enter the string: ') #'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    result = RLE(package_str)
    print(result)
    result2 = UNRLE(result)
    print(result2)


