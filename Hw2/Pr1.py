list_1=input('Введите первый список, разделяя элементы списка пробелом').split()
list_2=input('Введите второй список, разделяя элементы списка пробелом').split()
list_res=[] # создаем результирующий список
for i in range(len(list_1)):
    list_res.append(list_1[i])# добавляем  элемент из первого списка
    list_res.append(list_2[i]) # Добавляем элемент из 2го списка
print(*list_res) # выводим результирующий список