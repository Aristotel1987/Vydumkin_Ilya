list_files=['text.txt', 'text2.txt'] # Создаем список файлов для проверки
def merge_files(list_f, add_f=True): # Определяем функцию
    full_text='' # Создаем строку для сбора текста
    for i in list_f: # Перебираем файлы из списка
        with open(i, 'r') as f: # открываем файл для чтения
           lines=f.readlines()#считываем строки в переменную lines
           for line in lines:
               full_text+=line #Собираем в fulltext  zzсодержиимое строк
    if add_f==True: # Проверяем, нужно ли записывать результат в файл
        with open('fulltext.txt', 'w') as ft: # Открываем/создаем файлдля записи результата
            ft.write(full_text)# Записываем результат в файл
    return full_text # ВыВозвращаем результат из функции
print(merge_files(list_files)) # Распечатываем результат функции для проверки