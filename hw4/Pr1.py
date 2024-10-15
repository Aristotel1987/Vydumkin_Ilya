file = 'text.txt' #input('ВВедите название файла для сканирования')
import re  # импортируем модуль для работы с регулярными выражениями

full_text = ''  # Создаем строку для сбора текста
email_list, tel_list = [], []  # Создаем списки для имейлов и телефонов
with open(file, 'r') as f:  # открываем файл для чтения
    lines = f.readlines()  # считываем строки в переменную lines
for line in lines:  # Обрабатываем текст по строкам
    for i in line.split():  # разбиваем строку на слова и перебираем списокстрок
        if not i[-1].isalnum():  # проверяем последний символ на то, что он не буква, цифра
            i = i[:-1]  # Откидываем последний символ
        if re.match(r'[\w\.-]+@[\w\.-]+\.\w+', i):  # проверяем слово на наличие @
            email_list.append(i)  # добавляем слово в список емейлов
        if re.match(r'[7-8]{1}[0-9]{9}', i) and len(i) == 11:
            tel_list.append(i) # Добавляем слово в список телефонов
with open('result.txt', 'w') as rf:  # Открываем/создаем файл для записи результата
    rf.write('Список электронных адресов:\n') # Записываем результат в файл
    for k in email_list:
        rf.write(k+'\n')
    rf.write('Список телефонов:\n')
    for l in tel_list:
        rf.write(l+'\n')