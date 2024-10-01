
persons = [('John', 27), ('Nick', 15), ('Kate', 25)]
print(persons)
persons_adult=[] # Создаем список взрослых
for i in persons:
    if i[1]>=18: # Отбираем взрослых из общего списка
        persons_adult.append(i) #Добавляем отобранные элементы  к списку взрослых
persons_adult.sort(key=lambda i: i[1]) # Сортируем список взрослых, для внутреннней сортировки, используем лямбда выражение. 
# Альтернативный способ, без использования лямбда выражений, использовать функцию itemgetter  из модуля operator
#from operator import itemgetter
#persons_adult.sort(key=itemgetter(1))
print(persons_adult)