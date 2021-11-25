# 6.2.py
# Хімчинський Орест
# Лабораторна робота No 6.2
# Пошук елементів одновимірного масиву
# Варіант 15
import random


# створення масиву
def create(n):
    a = []
    for i in range(n):
        number = int(random.random() * 10)
        a.append(number)
    return a

# визначення найменшого та найбільшого значення із масиву
def high_and_low_number(a):
    high_and_low_list = []
    a = sorted(a)
    low = a[0]
    high = a[len(a)-1]
    high_and_low_list.append(low)
    high_and_low_list.append(high)
    return high_and_low_list
# розрахунки
def calculation(high_and_low_list):
    sum = high_and_low_list[0]+high_and_low_list[1]
    return sum


# головна функція
def main():
    a = create(15)
    print('Масив:', a)
    high_and_low_list = high_and_low_number(a)
    summ = calculation(high_and_low_list)
    print('Сума найбільшого та найменшого значення масиву: ', summ)


main()
