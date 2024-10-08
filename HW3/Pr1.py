list1=input('ВВедите список чисел, разделяя элементы пробелом').split() #ВВодим список для обработки
list_cube=list(map(lambda x: int(x)**3, list1)) #Вводим лист кубов первоначального списка
list_even=list(filter(lambda x: x%2==0, list_cube)) # Создаем список четных элементов
from functools import reduce  # Импортируем reduce из модуля functools
product = reduce(lambda x, y: x * y, list_even) # считаем произведение списка четных кубов через reduce
print(product) # выводим на экран произведение четных кубов