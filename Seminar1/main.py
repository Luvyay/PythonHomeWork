def Task1():
    # Найдите сумму цифр трехзначного числа. 

    number = int(input("Please enter the number: "))

    result = 0

    while(number > 0):
        result += number % 10
        number //= 10
    
    print(f"Sum equal {result}.")

def Task2():
    # Петя, Катя и Сережа делают из бумаги журавликов. Вместе
    # они сделали S журавликов. Сколько журавликов сделал каждый
    # ребенок, если известно, что Петя и Сережа сделали одинаковое
    # количество журавликов, а Катя сделала в два раза больше журавликов,
    # чем Петя и Сережа вместе?

    total_value = int(input("Please enter the total value: "))

    value_of_Petya_and_Sergey = total_value / 6
    value_of_Katya = total_value - value_of_Petya_and_Sergey * 2

    print(f"Petya did {int(value_of_Petya_and_Sergey)}; Sergey did {int(value_of_Petya_and_Sergey)}; Katya did {int(value_of_Katya)}")

def Task3():
    # Вы пользуетесь общественным транспортом? Вероятно, вы
    # расплачивались за проезд и получали билет с номером. Счастливым
    # билетом называют такой билет с шестизначным номером, где сумма
    # первых трех цифр равна сумме последних трех. Т.е. билет с номером
    # 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
    # программу, которая проверяет счастливость билета.

    number_of_ticket = int(input("Please enter the number of ticket: "))

    sum_left = 0
    sum_right = 0

    for i in range(0, 6):
        if i >= 3:
            sum_left += number_of_ticket % 10
        else:
            sum_right += number_of_ticket % 10
        
        number_of_ticket //= 10
    
    if sum_left == sum_right:
        print("This ticket is lucky!")
    else:
        print("This ticket isn't lucky.")

def Task4():
    # Требуется определить, можно ли от шоколадки размером n
    # × m долек отломить k долек, если разрешается сделать один разлом по
    # прямой между дольками (то есть разломить шоколадку на два
    # прямоугольника).

    columns = int(input("Please enter the columns of chocolate: "))
    rows = int(input("Please enter the rows of chocolate: "))
    cloves = int(input("Please enter the cloves: "))

    if (cloves % columns == 0 or cloves % rows == 0) and cloves <= columns * rows:
        print("Yes.")
    else:
        print("No.")

