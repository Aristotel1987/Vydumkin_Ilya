uneven=[i for i in range(1,60,2)] # Создаем список от1 до 60 нечетных чмсел
print([ i for i in uneven if (i%3==0 or i%5==0) and i%15!=0]) # Выводим числа  делящиеся на 3 и 5 и неделящиеся при этом на 15
print(uneven[-1]) # Выводим последний элемент первоначального списка